#!/usr/bin/env python3
"""Preview DOI metadata as BibTeX; use --write to append it to HanLab's bibliography.

Uses DOI content negotiation, documented at:
https://www.crossref.org/documentation/retrieve-metadata/content-negotiation/
Only Python's standard library is required.
"""

import argparse
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen


DEFAULT_FILE = Path(__file__).resolve().parents[1] / "_bibliography" / "papers.bib"
ENTRY_START = re.compile(r"@([A-Za-z]+)\s*([({])")


def normalize_doi(value):
    value = value.strip()
    if re.match(r"https?://", value, re.I):
        parts = urlsplit(value)
        if parts.hostname not in {"doi.org", "dx.doi.org", "www.doi.org"}:
            raise ValueError("Use a DOI or a https://doi.org/... link.")
        value = unquote(parts.path.lstrip("/"))
    value = re.sub(r"^doi\s*:\s*", "", value, flags=re.I)
    if not re.fullmatch(r"10\.\d{4,9}/\S+", value) or any(c in value for c in "\x00\r\n"):
        raise ValueError("Invalid DOI. Expected a value such as 10.1038/nature14539.")
    return value


def entries(text):
    """Find balanced BibTeX entries, including entries with nested TeX braces."""
    result = []
    cursor = 0
    while match := ENTRY_START.search(text, cursor):
        opening = match.group(2)
        depth = 1 if opening == "{" else 0
        quoted = False
        index = match.end()
        while index < len(text):
            char = text[index]
            if char == "\\":
                index += 2
                continue
            if char == '"' and depth == 0:
                quoted = not quoted
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth < 0:
                    raise ValueError("Unbalanced braces in bibliography; no changes made.")
                if opening == "{" and depth == 0:
                    break
            elif char == ")" and opening == "(" and depth == 0 and not quoted:
                break
            index += 1
        else:
            raise ValueError("Unclosed BibTeX entry; no changes made.")
        cursor = index + 1
        if match.group(1).lower() in {"comment", "string", "preamble"}:
            continue
        body = text[match.end():index]
        key, separator, _ = body.partition(",")
        key = key.strip()
        if not separator or not key or re.search(r"\s|[{}()\"#%]", key):
            raise ValueError("Invalid BibTeX entry key; no changes made.")
        result.append((key, text[match.start():cursor]))
    return result


def field_values(entry, field):
    pattern = re.compile(
        r"\b" + re.escape(field) + r"\s*=\s*(?:\{([^{}]*)\}|\"([^\"]*)\"|([^,\s}]+))",
        re.I,
    )
    return [next(value for value in match.groups() if value is not None).strip()
            for match in pattern.finditer(entry)]


def contains_doi(entry, doi):
    for value in field_values(entry, "doi") + field_values(entry, "url"):
        try:
            if normalize_doi(value).casefold() == doi.casefold():
                return True
        except ValueError:
            pass
    return False


def fetch_bibtex(doi, timeout):
    request = Request(
        "https://doi.org/" + quote(doi, safe="/"),
        headers={"Accept": "application/x-bibtex", "User-Agent": "HanLab-DOI-Importer/1.0"},
    )
    with urlopen(request, timeout=timeout) as response:
        payload = response.read(2_000_001)
        if len(payload) > 2_000_000:
            raise ValueError("Metadata response was too large; no changes made.")
        result = payload.decode(response.headers.get_content_charset() or "utf-8").strip()
    records = entries(result)
    if len(records) != 1 or result != records[0][1]:
        raise ValueError("The DOI service did not return one valid BibTeX entry.")
    returned_dois = field_values(result, "doi")
    if returned_dois and not any(normalize_doi(value).casefold() == doi.casefold() for value in returned_dois):
        raise ValueError("Returned DOI does not match the requested DOI; no changes made.")
    if not returned_dois:
        result = result[:-1].rstrip().rstrip(",") + ",\n  doi = {" + doi + "}\n" + result[-1]
    return result


def append_atomically(path, original, entry):
    newline = b"\r\n" if b"\r\n" in original else b"\n"
    suffix = entry.replace("\r\n", "\n").replace("\n", newline.decode()).encode("utf-8")
    updated = original + (newline * 2 if original else b"") + suffix + newline
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".doi-import-", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(updated)
            handle.flush()
            os.fsync(handle.fileno())
        if path.exists():
            if path.read_bytes() != original:
                raise ValueError("Bibliography changed during import. Please rerun the command.")
            os.chmod(temporary, path.stat().st_mode)
        elif original:
            raise ValueError("Bibliography was removed during import. Please rerun the command.")
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("doi", help="DOI or https://doi.org/... URL")
    parser.add_argument("--file", type=Path, default=DEFAULT_FILE, help="BibTeX file (default: _bibliography/papers.bib)")
    parser.add_argument("--write", action="store_true", help="Append metadata; without this flag, preview only")
    parser.add_argument("--key", help="Override citation key, for example Han2026Healthcare")
    parser.add_argument("--timeout", type=float, default=25, help="Network timeout in seconds (default: 25)")
    args = parser.parse_args()
    try:
        doi = normalize_doi(args.doi)
        if args.timeout <= 0:
            raise ValueError("Timeout must be positive.")
        path = args.file.expanduser().resolve()
        original = path.read_bytes() if path.exists() else b""
        existing = entries(original.decode("utf-8-sig"))
        if any(contains_doi(entry, doi) for _, entry in existing):
            print(f"Already present: {doi}. No changes made.", file=sys.stderr)
            return 0
        entry = fetch_bibtex(doi, args.timeout)
        if args.key:
            if not re.fullmatch(r"[A-Za-z0-9_:.+-]+", args.key):
                raise ValueError("Use letters, numbers, _, :, ., + or - in a citation key.")
            entry = re.sub(r"^(@[A-Za-z]+\s*[({])\s*[^,]+", lambda match: match.group(1) + args.key, entry, count=1)
        key = entries(entry)[0][0]
        if key.casefold() in {existing_key.casefold() for existing_key, _ in existing}:
            raise ValueError(f"Citation key '{key}' already exists. Rerun with --key NEW_KEY.")
        if args.write:
            append_atomically(path, original, entry)
            print(f"Added {doi} as {key} to {path}")
        else:
            print(entry)
            print("Preview only. Check the metadata, then add --write to append it.", file=sys.stderr)
        return 0
    except (OSError, UnicodeError, ValueError, HTTPError, URLError) as error:
        print(f"Import failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
