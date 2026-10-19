---
layout: page
title: News
permalink: /news/
description: Research and academic updates involving Jing Han and collaborators
nav: true
nav_order: 4
---

<link rel="stylesheet" href="{{ '/assets/css/hanlab-content.css' | relative_url }}">

Research publications, resources and academic activities, including selected updates from Jing Han's earlier work.

{% if site.news.size > 0 %}
{% include news.liquid %}
{% else %}

Lab news and announcements will be added here.

{% endif %}
