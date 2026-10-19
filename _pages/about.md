---
layout: about
title: Home
permalink: /
subtitle: AI for healthcare, audio &amp; non-audio learning · Hunan University

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
[**Professor Jing Han (韩静)**]({{ '/' | relative_url }}#jing-han).
We study how artificial intelligence can learn from audio and other human signals to support health and wellbeing.

<h2 id="jing-han">Professor Jing Han</h2>

Professor Jing Han is a professor in the School of Computer Science at Hunan University and leads HanLab.
Her work connects mobile and intelligent healthcare with audio, physiological signals, multimodal learning and deep learning.

Previously, she worked with Professor Cecilia Mascolo at the University of Cambridge.
She earned her doctorate at the University of Augsburg in 2020, her master's degree at Nanyang Technological University in 2014,
and her bachelor's degree at Harbin Engineering University in 2011.
Her earlier research and education are documented in her [Cambridge profile](https://www.cst.cam.ac.uk/people/jh2298).

Her academic service includes journal editing and guest editorship; her [activities page](https://sites.google.com/view/jinghan/activities)
lists these roles and invited talks.
Her recognition includes the [2024 Heroines of Science selection](https://www.postdocacademy.cam.ac.uk/news/heroines-science-winners),
membership in a Cambridge team receiving the [2021 Better Future Award](https://www.cst.cam.ac.uk/ring/awards),
and an [AAAC Outstanding PhD Dissertation Award honourable mention](https://www.schuller.it/bws/?page_id=115).

[University profile](https://csee.hnu.edu.cn/people/hanjing) ·
[Google Scholar](https://scholar.google.com/citations?user=90uh0GcAAAAJ&hl=en) ·
[ORCID](https://orcid.org/0000-0001-5776-6849) ·
[DBLP](https://dblp.org/pid/90/2562-10.html) ·
[Personal website](https://sites.google.com/view/jinghan) ·
[People]({{ '/people/' | relative_url }})

<div class="clearfix"></div>

## The meaning of HanLab

<div class="row row-cols-1 row-cols-md-3">
  <div class="col mb-3"><div class="card h-100"><div class="card-body"><h3 class="card-title">H · Healthcare</h3><p class="card-text">AI for mobile health, respiratory and cardiac sounds, and physiological signals.</p></div></div></div>
  <div class="col mb-3"><div class="card h-100"><div class="card-body"><h3 class="card-title">a · Audio</h3><p class="card-text">Learning from speech, everyday sounds, and other acoustic signals.</p></div></div></div>
  <div class="col mb-3"><div class="card h-100"><div class="card-body"><h3 class="card-title">n · Non-audio</h3><p class="card-text">Understanding complementary physiological and other sensor data.</p></div></div></div>
</div>

Explore our [research and collaborative projects]({{ '/research/' | relative_url }}) and
[publications]({{ '/publications/' | relative_url }}), including earlier work by Jing Han and collaborators.

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
