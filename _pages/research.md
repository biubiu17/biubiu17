---
layout: page
title: Research
permalink: /research/
description: Healthcare, audio & non-audio
nav: true
nav_order: 1
---

## Healthcare

Our research interests include questions in healthcare.

## Audio & non-audio

We study audio and non-audio data.

## Projects

{% if site.projects.size > 0 %}
{% assign sorted_projects = site.projects | sort: 'importance' %}

<div class="projects">
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>
{% else %}

Project details will be added here.

{% endif %}
