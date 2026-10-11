---
layout: page
permalink: /publications/
title: Publications
description: Selected and recent publications by Jing Han and collaborators
nav: true
nav_order: 2
---

This collection brings together recent and representative publications by **Jing Han and collaborators**, including work at previous institutions.
For the broader publication record, visit [Google Scholar](https://scholar.google.com/citations?user=90uh0GcAAAAJ&hl=en)
or [DBLP](https://dblp.org/pid/90/2562-10.html).

{% capture publication_count %}{% bibliography_count %}{% endcapture %}
{% assign publication_count = publication_count | plus: 0 %}
{% if publication_count > 0 %}
{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>
{% else %}

The publication list will be added here.

{% endif %}
