---
layout: about
title: Home
permalink: /
subtitle: AI for health, audio &amp; multimodal understanding · Hunan University

# The verified university portrait gives the homepage a human focal point.
# Replace it with an authorised group photograph when one is available.
profile:
  align: right
  image: jing-han.jpg
  image_circular: false
selected_papers: true
social: true

announcements:
  enabled: true
  scrollable: true
  limit: 3

latest_posts:
  enabled: false
  scrollable: true
  limit: 3
---

**HanLab** is a research group at the **School of Computer Science, Hunan University**, led by
**[Professor Jing Han (韩静)]({{ '/people/' | relative_url }})**.
We study how artificial intelligence can learn from audio and other human signals to support health and wellbeing.

湖南大学计算机学院 · HanLab

## What we study

- **Intelligent healthcare:** mobile health, respiratory and cardiac sound analysis, and physiological signal understanding.
- **Audio & non-audio learning:** representation learning across speech, sounds and other sensing modalities.
- **Multimodal affective computing:** emotion recognition and sentiment understanding from complementary signals.

Explore our [research and collaborative projects]({{ '/research/' | relative_url }}) and
[publications]({{ '/publications/' | relative_url }}), including earlier work by Jing Han and collaborators.

<div class="clearfix"></div>

## Open research resources

{% assign featured_projects = site.projects | sort: 'importance' %}
<div class="projects">
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in featured_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>

## Get in touch

For research enquiries, contact [jhan@hnu.edu.cn](mailto:jhan@hnu.edu.cn).
