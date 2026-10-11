$ErrorActionPreference = 'Stop'
$siteRoot = Split-Path -Parent $PSScriptRoot
$portableEnv = Join-Path (Split-Path -Parent $siteRoot) 'tmp/alfolio-tools/env.ps1'
if (Test-Path -LiteralPath $portableEnv) {
    . $portableEnv
}
if (-not (Get-Command bundle -ErrorAction SilentlyContinue)) {
    throw 'Ruby / Bundler was not found. See docs/HANLAB-GUIDE.md for setup on another computer.'
}
Set-Location -LiteralPath $siteRoot
$env:JEKYLL_ENV = 'development'
Write-Host 'HanLab preview: http://localhost:4000/al-folio/' -ForegroundColor Cyan
Write-Host 'Wait for Server running. Press Ctrl+C to stop.'
bundle exec jekyll serve --host 127.0.0.1 --port 4000 --baseurl /al-folio --watch --force_polling
if ($LASTEXITCODE -ne 0) {
    throw "Jekyll exited with code $LASTEXITCODE"
}
