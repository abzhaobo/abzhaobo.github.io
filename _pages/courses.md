---
layout: page
title: Courses
permalink: /courses/
description:
nav: true
nav_order: 2
display_categories: [Under development, 2025, Earlier]
horizontal: false
---

The comment system went live in September 2025 (a bit late). You're very welcome to leave comments or questions at the bottom of each course page. Your feedback not only helps me improve the course, but also gives me the motivation to keep going. Knowing that these courses matter to you means more to me than words can express.

<!-- pages/courses.md -->
<div class="courses">
{% if site.enable_course_categories and page.display_categories %}
  <!-- Display categorized courses -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_courses = site.courses | where: "category", category %}
  {% assign sorted_courses = categorized_courses | sort: "importance" %}
  <!-- Generate cards for each course -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for course in sorted_courses %}
      {% include courses_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for course in sorted_courses %}
      {% include courses.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display courses without categories -->

{% assign sorted_courses = site.courses | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for course in sorted_courses %}
      {% include courses_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for course in sorted_courses %}
      {% include courses.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>

---

<h4>Warnings hanging over my head:</h4>

> Students are taught minor details in statistics when the hard business of quantitative thinking in economics is getting the data straight; they are taught minor details in mathematics when the hard business of mathematical economics is getting economic ideas straight. (In fact they are often taught mistaken details: that statistical significance, for example, has anything to do with substantive significance; or that a proof on a blackboard is the same thing as a proof in the world [McCloskey 1998; McCloskey and Ziliak 1996]). In most schools they are taught nothing about writing, when the hard business of economic thinking is getting the words straight.
>
> <cite> -- Deirdre N. McCloskey </cite>