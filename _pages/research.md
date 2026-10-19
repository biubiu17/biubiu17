---
layout: page
title: Research
permalink: /research/
description: Healthcare, audio and non-audio learning
nav: true
nav_order: 1
_styles: |
  .post article > h2 { margin-top: 3.5rem; margin-bottom: 1.25rem; }
  .post article > h2:first-of-type { margin-top: 1rem; }
---

<link rel="stylesheet" href="{{ '/assets/css/hanlab-content.css' | relative_url }}">

## AI for health and wellbeing

Our interests span mobile and intelligent healthcare, from respiratory and cardiac sounds to physiological signals.
Related work explores audio monitoring, health-related representations and reproducible evaluation across datasets.
See the [OPERA]({{ '/projects/opera/' | relative_url }}) and [Tyee]({{ '/projects/tyee/' | relative_url }}) collaborations.

## Audio & non-audio learning

We are interested in learning useful representations from speech, environmental sounds and non-audio sensing modalities.
This includes foundation models, transfer across tasks and efficient training pipelines.
[AudioFab]({{ '/projects/audiofab/' | relative_url }}) explores how an agent can select and coordinate audio tools from natural-language instructions.

## Non-audio sensing and multimodal learning

We study physiological signals and other non-audio measurements alongside sound, connecting complementary sources of information
for health-related tasks. This includes representation learning and reliable evaluation across sensing modalities.
Relevant papers are listed on the [Publications]({{ '/publications/' | relative_url }}) page.

## Collaborative projects & open resources

These projects involve Jing Han and collaborators across institutions, including work undertaken before HanLab at Hunan University.
Each page links to the original paper and project maintainers.

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
