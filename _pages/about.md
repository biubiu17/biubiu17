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
# Render the two sections below with explicit, consistently capitalised headings.
selected_papers: false
social: true

announcements:
  enabled: false
  scrollable: true
  limit: 3

latest_posts:
  enabled: false
  scrollable: true
  limit: 3
---

<link rel="stylesheet" href="{{ '/assets/css/hanlab-content.css' | relative_url }}">

<style>
  .post article > .clearfix > h2,
  .post article > h2 {
    margin-top: 3.25rem;
    margin-bottom: 1.35rem;
  }
  .hanlab-pillar-row { margin-top: 1.25rem; margin-bottom: 1.75rem; }
  .hanlab-pillar {
    background: var(--pillar-bg);
    border: 1px solid color-mix(in srgb, var(--pillar-accent) 18%, transparent);
    border-radius: .75rem;
    box-shadow: 0 5px 16px rgba(24, 46, 57, .06);
  }
  .hanlab-pillar .card-body { padding: 1.5rem; }
  .hanlab-pillar .card-title { color: var(--pillar-accent); font-size: 1.4rem; }
  .hanlab-pillar .card-text { color: #253c42; }
  .hanlab-pillar--health { --pillar-bg: #e8f4ee; --pillar-accent: #1b6b56; }
  .hanlab-pillar--audio { --pillar-bg: #edf2fb; --pillar-accent: #345d9d; }
  .hanlab-pillar--non-audio { --pillar-bg: #fff2e8; --pillar-accent: #96552d; }
  .hanlab-letter-h { color: #1b6b56; }
  .hanlab-letter-a { color: #345d9d; }
  .hanlab-letter-n { color: #96552d; }
  html[data-theme="dark"] .hanlab-pillar .card-text { color: #e8f0f2; }
  html[data-theme="dark"] .hanlab-pillar--health { --pillar-bg: #17362e; --pillar-accent: #9de0c2; }
  html[data-theme="dark"] .hanlab-pillar--audio { --pillar-bg: #202e48; --pillar-accent: #a9c4fc; }
  html[data-theme="dark"] .hanlab-pillar--non-audio { --pillar-bg: #3d2d25; --pillar-accent: #f1bd98; }
  html[data-theme="dark"] .hanlab-letter-h { color: #9de0c2; }
  html[data-theme="dark"] .hanlab-letter-a { color: #a9c4fc; }
  html[data-theme="dark"] .hanlab-letter-n { color: #f1bd98; }
</style>

**HanLab** is a research group at the **School of Computer Science, Hunan University**, led by
[**Professor Jing Han (韩静)**]({{ '/' | relative_url }}#jing-han).
We study how artificial intelligence can learn from audio and other human signals to support health and wellbeing.

<h2 id="jing-han">Professor Jing Han</h2>

**Role & research.** Jing Han is a professor in the School of Computer Science at Hunan University and leads HanLab.
Her research connects healthcare with audio, physiological signals, multimodal learning and deep learning.

**Education & research experience.** She received her PhD from the University of Augsburg, Germany, in 2020,
supervised by [Professor Björn W. Schuller](https://www.schuller.one/).
She subsequently conducted postdoctoral research on wearable sensing and mobile health at the University of Cambridge,
working with [Professor Cecilia Mascolo](https://www.cl.cam.ac.uk/~cm542/).
She received her master's degree from Nanyang Technological University, Singapore, in 2014, and her bachelor's degree
in Electronic and Information Engineering from Harbin Engineering University, China, in 2011.

**Academic service.** She serves as an Associate Editor of _IEEE Transactions on Affective Computing_ and reviews for
_IEEE Transactions on Cybernetics_, _IEEE Signal Processing Magazine_ and _IEEE Transactions on Multimedia_.
She co-organised special sessions at ICASSP 2022 and INTERSPEECH 2021, and has served as a session chair or programme
committee member at international conferences.

**Selected recognition.** Honourable Mention, AAAC Outstanding PhD Dissertation Award (2021);
member of the Cambridge research team receiving the Better Future Award (2021).

[University profile](https://csee.hnu.edu.cn/people/hanjing) ·
[Google Scholar](https://scholar.google.com/citations?user=90uh0GcAAAAJ&hl=en) ·
[ORCID](https://orcid.org/0000-0001-5776-6849) ·
[DBLP](https://dblp.org/pid/90/2562-10.html) ·
[Personal website](https://sites.google.com/view/jinghan) ·
[People]({{ '/people/' | relative_url }})

<div class="clearfix"></div>

<h2>The meaning of <span class="hanlab-letter-h">H</span><span class="hanlab-letter-a">a</span><span class="hanlab-letter-n">n</span>Lab</h2>

<div class="row row-cols-1 row-cols-md-3 hanlab-pillar-row">
  <div class="col mb-3"><div class="card h-100 hanlab-pillar hanlab-pillar--health"><div class="card-body"><h3 class="card-title">H · Healthcare</h3><p class="card-text">AI for mobile health, respiratory and cardiac sounds, and physiological signals.</p></div></div></div>
  <div class="col mb-3"><div class="card h-100 hanlab-pillar hanlab-pillar--audio"><div class="card-body"><h3 class="card-title">a · Audio</h3><p class="card-text">Learning from speech, everyday sounds, and other acoustic signals.</p></div></div></div>
  <div class="col mb-3"><div class="card h-100 hanlab-pillar hanlab-pillar--non-audio"><div class="card-body"><h3 class="card-title">n · Non-audio</h3><p class="card-text">Understanding complementary physiological and other sensor data.</p></div></div></div>
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

<h2><a href="{{ '/news/' | relative_url }}" style="color: inherit">News</a></h2>

{% include news.liquid limit=true %}

<h2><a href="{{ '/publications/' | relative_url }}" style="color: inherit">Selected Publications</a></h2>

{% include selected_papers.liquid %}
