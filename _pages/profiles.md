---
layout: page
permalink: /people/
title: People
description: Faculty and students at HanLab
nav: true
nav_order: 3
_styles: |
  .hanlab-carousel {
    position: relative;
    width: 100%;
    margin: 0 0 2.25rem;
    padding-bottom: 1.75rem;
  }
  .hanlab-carousel-radio {
    appearance: none;
    position: absolute;
    bottom: .35rem;
    width: .8rem;
    height: .8rem;
    border: 1px solid #637586;
    border-radius: 50%;
    cursor: pointer;
  }
  .hanlab-carousel-radio:checked { background: #526f83; }
  .hanlab-carousel-radio:focus-visible { outline: 3px solid #bd4caa; outline-offset: 3px; }
  #hanlab-photo-1 { left: calc(50% - 2rem); }
  #hanlab-photo-2 { left: calc(50% - .4rem); }
  #hanlab-photo-3 { left: calc(50% + 1.2rem); }
  .hanlab-slide { display: none; margin: 0; }
  #hanlab-photo-1:checked ~ .hanlab-slides .hanlab-slide-1,
  #hanlab-photo-2:checked ~ .hanlab-slides .hanlab-slide-2,
  #hanlab-photo-3:checked ~ .hanlab-slides .hanlab-slide-3 { display: block; }
  .hanlab-slide-image { position: relative; }
  .hanlab-slide img {
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 12 / 5;
    object-fit: cover;
    border-radius: .4rem;
  }
  .hanlab-slide figcaption {
    font-size: .95rem;
    text-align: center;
    padding: .7rem .1rem 0;
  }
  .hanlab-carousel-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    display: grid;
    place-items: center;
    width: 2.75rem;
    height: 2.75rem;
    border-radius: 50%;
    background: rgba(10, 26, 43, .78);
    color: white;
    font-size: 1.35rem;
    cursor: pointer;
    user-select: none;
  }
  .hanlab-carousel-arrow:hover { background: rgba(10, 26, 43, .95); }
  .hanlab-carousel-arrow span[aria-hidden="true"] { color: #fff; }
  .hanlab-carousel-prev { left: .8rem; }
  .hanlab-carousel-next { right: .8rem; }
  .hanlab-sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
  }
  @media (max-width: 575px) {
    .hanlab-carousel-arrow { width: 2.25rem; height: 2.25rem; }
  }
---

<link rel="stylesheet" href="{{ '/assets/css/hanlab-content.css' | relative_url }}">

<div class="hanlab-carousel" role="group" aria-label="HanLab photo gallery">
  <input class="hanlab-carousel-radio" type="radio" id="hanlab-photo-1" name="hanlab-photo" aria-label="Show image 1 of 3" checked>
  <input class="hanlab-carousel-radio" type="radio" id="hanlab-photo-2" name="hanlab-photo" aria-label="Show image 2 of 3">
  <input class="hanlab-carousel-radio" type="radio" id="hanlab-photo-3" name="hanlab-photo" aria-label="Show image 3 of 3">
  <div class="hanlab-slides">
    <figure class="hanlab-slide hanlab-slide-1">
      <div class="hanlab-slide-image">
        <img src="{{ '/assets/img/people/gallery-group.svg' | relative_url }}" alt="Placeholder for a future HanLab group photo" width="960" height="400">
        <label class="hanlab-carousel-arrow hanlab-carousel-prev" for="hanlab-photo-3" title="Previous image"><span aria-hidden="true">&#10094;</span><span class="hanlab-sr-only">Previous image</span></label>
        <label class="hanlab-carousel-arrow hanlab-carousel-next" for="hanlab-photo-2" title="Next image"><span aria-hidden="true">&#10095;</span><span class="hanlab-sr-only">Next image</span></label>
      </div>
      <figcaption>Our group · 1 / 3</figcaption>
    </figure>
    <figure class="hanlab-slide hanlab-slide-2">
      <div class="hanlab-slide-image">
        <img src="{{ '/assets/img/people/gallery-research.svg' | relative_url }}" alt="Placeholder for future research activity photos" width="960" height="400">
        <label class="hanlab-carousel-arrow hanlab-carousel-prev" for="hanlab-photo-1" title="Previous image"><span aria-hidden="true">&#10094;</span><span class="hanlab-sr-only">Previous image</span></label>
        <label class="hanlab-carousel-arrow hanlab-carousel-next" for="hanlab-photo-3" title="Next image"><span aria-hidden="true">&#10095;</span><span class="hanlab-sr-only">Next image</span></label>
      </div>
      <figcaption>Research moments · 2 / 3</figcaption>
    </figure>
    <figure class="hanlab-slide hanlab-slide-3">
      <div class="hanlab-slide-image">
        <img src="{{ '/assets/img/people/gallery-community.svg' | relative_url }}" alt="Placeholder for future lab event photos" width="960" height="400">
        <label class="hanlab-carousel-arrow hanlab-carousel-prev" for="hanlab-photo-2" title="Previous image"><span aria-hidden="true">&#10094;</span><span class="hanlab-sr-only">Previous image</span></label>
        <label class="hanlab-carousel-arrow hanlab-carousel-next" for="hanlab-photo-1" title="Next image"><span aria-hidden="true">&#10095;</span><span class="hanlab-sr-only">Next image</span></label>
      </div>
      <figcaption>Lab life · 3 / 3</figcaption>
    </figure>
  </div>
</div>

<div class="hanlab-team">
  <section class="hanlab-member-group" aria-labelledby="group-professor">
    <h2 id="group-professor">Professor</h2>
    <div class="hanlab-member-grid">
      <div class="hanlab-member hanlab-member-pi">
        <a class="hanlab-member-profile" href="{{ '/' | relative_url }}#jing-han" aria-label="Professor Jing Han — profile on Home">
          <img src="{{ '/assets/img/jing-han.jpg' | relative_url }}" alt="Professor Jing Han" width="176" height="176">
          <h3>Jing Han</h3>
        </a>
        <p class="hanlab-member-meta">Director of HanLab</p>
        <div class="hanlab-member-links">
          <a href="mailto:jhan@hnu.edu.cn" aria-label="Email Jing Han" title="Email"><i class="fa-solid fa-envelope" aria-hidden="true"></i></a>
          <a href="https://scholar.google.com/citations?user=90uh0GcAAAAJ&amp;hl=en" aria-label="Google Scholar: Jing Han" title="Google Scholar"><i class="ai ai-google-scholar" aria-hidden="true"></i></a>
        </div>
      </div>
    </div>
  </section>
  {% include_relative people_students.md %}
</div>
