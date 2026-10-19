---
layout: page
permalink: /people/
title: People
description: The people behind HanLab
nav: true
nav_order: 3
_styles: |
  .hanlab-gallery {
    display: flex;
    gap: 1rem;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    padding: .25rem .15rem 1rem;
  }
  .hanlab-gallery figure {
    flex: 0 0 calc((100% - 2rem) / 3);
    min-width: 0;
    margin: 0;
    scroll-snap-align: start;
  }
  .hanlab-gallery img {
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 4 / 3;
    object-fit: cover;
    border-radius: .4rem;
  }
  .hanlab-gallery figcaption {
    font-size: .88rem;
    padding: .45rem .1rem 0;
  }
  .hanlab-pi {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin: 1rem 0 2.5rem;
  }
  .hanlab-pi img {
    width: 155px;
    height: 190px;
    object-fit: cover;
    border-radius: .4rem;
    flex-shrink: 0;
  }
  @media (max-width: 575px) {
    .hanlab-gallery figure { flex-basis: 82%; }
    .hanlab-pi { align-items: flex-start; gap: 1rem; }
    .hanlab-pi img { width: 105px; height: 132px; }
  }
---

<div class="hanlab-gallery" aria-label="Future HanLab group photos; swipe to see more">
  <figure>
    <img src="{{ '/assets/img/people/gallery-group.svg' | relative_url }}" alt="Placeholder for a future HanLab group photo" width="600" height="450">
    <figcaption>Our group</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/img/people/gallery-research.svg' | relative_url }}" alt="Placeholder for future research activity photos" width="600" height="450">
    <figcaption>Research moments</figcaption>
  </figure>
  <figure>
    <img src="{{ '/assets/img/people/gallery-community.svg' | relative_url }}" alt="Placeholder for future lab event photos" width="600" height="450">
    <figcaption>Lab life</figcaption>
  </figure>
</div>

## Principal Investigator

<div class="hanlab-pi">
  <img src="{{ '/assets/img/jing-han.jpg' | relative_url }}" alt="Professor Jing Han" width="155" height="190">
  <div>
    <h3>Professor Jing Han</h3>
    <p>Professor, School of Computer Science, Hunan University<br>Director of HanLab</p>
    <p><a href="{{ '/' | relative_url }}#jing-han">Read her profile on Home &rarr;</a></p>
  </div>
</div>

{% capture doctoral_students %}{% include_relative people_doctoral_students.md %}{% endcapture %}
{{ doctoral_students | markdownify }}
