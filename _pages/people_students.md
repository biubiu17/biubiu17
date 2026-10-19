{% for group in site.data.member_groups %}
{% assign students = site.pages | where: 'member_group', group.id | sort: 'member_order' %}
{% if students.size > 0 %}
    <section class="hanlab-member-group" aria-labelledby="group-{{ group.id }}">
      <h2 id="group-{{ group.id }}">{{ group.title }}</h2>
      <div class="hanlab-member-grid">
        {% for student in students %}
          <div class="hanlab-member">
            <a class="hanlab-member-profile" href="{{ student.url | relative_url }}" aria-label="{{ student.title | escape }} — personal profile">
              <img
                src="{{ student.portrait | relative_url }}"
                alt="{{ student.portrait_alt | escape }}"
                width="152"
                height="152"
                loading="lazy"
              >
              <h3>{{ student.title }}</h3>
            </a>
            <p class="hanlab-member-meta">{{ group.position }}{% if student.cohort %} · {{ student.cohort }}{% endif %}</p>
            {% if student.email or student.scholar or student.github %}
              <div class="hanlab-member-links">
                {% if student.email %}<a href="mailto:{{ student.email | escape }}" aria-label="Email {{ student.title | escape }}" title="Email"><i class="fa-solid fa-envelope" aria-hidden="true"></i></a>{% endif %}
                {% if student.scholar %}<a href="{{ student.scholar | escape }}" aria-label="Google Scholar: {{ student.title | escape }}" title="Google Scholar"><i class="ai ai-google-scholar" aria-hidden="true"></i></a>{% endif %}
                {% if student.github %}<a href="{{ student.github | escape }}" aria-label="GitHub: {{ student.title | escape }}" title="GitHub"><i class="fa-brands fa-github" aria-hidden="true"></i></a>{% endif %}
              </div>
            {% endif %}
          </div>
        {% endfor %}
      </div>
    </section>
{% endif %}
{% endfor %}
