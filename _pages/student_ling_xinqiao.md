---
layout: page
title: 凌心乔
permalink: /people/ling-xinqiao/
description: Undergraduate Student · HanLab · Hunan University
nav: false
member_group: undergraduate
member_order: 1
cohort: 2026
portrait: /assets/img/people/default-avatar-circle.svg
portrait_alt: Default avatar — photo coming soon
---

<link rel="stylesheet" href="{{ '/assets/css/hanlab-content.css' | relative_url }}">

[← Back to People]({{ '/people/' | relative_url }})

<div class="row mt-4 mb-4">
  <div class="col-sm-4 mb-4">
    <img
      src="{{ page.portrait | relative_url }}"
      alt="{{ page.portrait_alt | escape }}"
      class="img-fluid rounded-circle"
      width="400"
      height="400"
      style="width: 100%; max-width: 260px; height: auto; aspect-ratio: 1; object-fit: cover;"
    >
  </div>
  <div class="col-sm-8">
    <h2>About</h2>
    <p>{{ page.title }} is an undergraduate student in HanLab at the School of Computer Science, Hunan University.</p>
    <dl>
      <dt>Position</dt>
      <dd>Undergraduate Student</dd>
      {% if page.cohort %}
        <dt>Cohort</dt>
        <dd>{{ page.cohort }}</dd>
      {% endif %}
      <dt>Research group</dt>
      <dd><a href="{{ '/' | relative_url }}">HanLab</a> · Hunan University</dd>
    </dl>
    <p><a href="{{ '/contact/' | relative_url }}">Lab contact information &rarr;</a></p>
  </div>
</div>

<!-- Add verified research interests, education, publications and personal contact links below. -->
