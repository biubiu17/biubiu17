## Doctoral Students

{% assign students = site.pages | where: 'member_group', 'doctoral' | sort: 'member_order' %}

<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3">
  {% for student in students %}
    <div class="col mb-4">
      <a class="d-block h-100" href="{{ student.url | relative_url }}" aria-label="{{ student.title | escape }} — personal profile">
        <div class="card h-100 hoverable">
          <img
            class="card-img-top"
            src="{{ student.portrait | relative_url }}"
            alt="{{ student.portrait_alt | escape }}"
            width="400"
            height="400"
            loading="lazy"
            style="width: 100%; height: auto; aspect-ratio: 1; object-fit: cover;"
          >
          <div class="card-body text-center">
            <h3 class="card-title">{{ student.title }}</h3>
            <p class="card-text">PhD Student · {{ student.cohort }}</p>
            <span>View profile &rarr;</span>
          </div>
        </div>
      </a>
    </div>
  {% endfor %}
</div>
