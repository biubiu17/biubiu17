---
layout: page
permalink: /publications/
title: Publications
description: Research publications from HanLab
nav: true
nav_order: 2
---

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
