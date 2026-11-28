---
layout: page
title: Courses 课程
permalink: /courses/
description:
nav: true
nav_order: 2
display_categories: [Current, Archive]
horizontal: false
---

Questions, corrections, or suggestions? Feel free to leave a comment on the course pages. Your feedback is essential for refining these course materials.

<!-- pages/courses.md -->
<div class="courses">
  {% assign current_courses = site.courses | where: "category", "Current" | sort: "importance" %}
  {% assign archive_courses = site.courses | where: "category", "Archive" | sort: "importance" | sort: "year" | reverse %}

  <div class="courses-tabs" role="tablist" aria-label="Course views">
    <button
      type="button"
      class="courses-tab active"
      role="tab"
      id="tab-current"
      aria-controls="panel-current"
      aria-selected="true"
      data-courses-tab="current"
    >
      Current <span class="courses-tab-count">{{ current_courses.size }}</span>
    </button>
    <button
      type="button"
      class="courses-tab"
      role="tab"
      id="tab-archive"
      aria-controls="panel-archive"
      aria-selected="false"
      data-courses-tab="archive"
    >
      Archive <span class="courses-tab-count">{{ archive_courses.size }}</span>
    </button>
  </div>

  <div id="panel-current" class="courses-panel" role="tabpanel" aria-labelledby="tab-current">
    <div class="course-compact-grid">
      {% for course in current_courses %}
        {% include courses_compact.liquid %}
      {% endfor %}
    </div>
  </div>

  <div id="panel-archive" class="courses-panel" role="tabpanel" aria-labelledby="tab-archive" hidden>
    <ul class="course-archive-list">
      {% for course in archive_courses %}
        {% if course.redirect %}
          {% assign course_url = course.redirect %}
        {% else %}
          {% assign course_url = course.url | relative_url %}
        {% endif %}
        <li class="course-archive-item">
          <span class="course-archive-date">{{ course.term | default: course.year }}</span>
          <a class="course-archive-title" href="{{ course_url }}">{{ course.title }}</a>
        </li>
      {% endfor %}
    </ul>
  </div>
</div>

<script>
  (function () {
    var tabButtons = document.querySelectorAll('[data-courses-tab]');
    var panels = {
      current: document.getElementById('panel-current'),
      archive: document.getElementById('panel-archive'),
    };
    if (!tabButtons.length || !panels.current || !panels.archive) return;

    function activateTab(target, syncHash) {
      var isArchive = target === 'archive';
      var activeKey = isArchive ? 'archive' : 'current';

      tabButtons.forEach(function (btn) {
        var matched = btn.getAttribute('data-courses-tab') === activeKey;
        btn.classList.toggle('active', matched);
        btn.setAttribute('aria-selected', matched ? 'true' : 'false');
      });

      panels.current.hidden = isArchive;
      panels.archive.hidden = !isArchive;

      if (syncHash && window.history && window.history.replaceState) {
        var nextUrl = isArchive
          ? window.location.pathname + window.location.search + '#archive'
          : window.location.pathname + window.location.search;
        window.history.replaceState(null, '', nextUrl);
      }
    }

    tabButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        activateTab(btn.getAttribute('data-courses-tab'), true);
      });
    });

    function syncFromHash() {
      activateTab(window.location.hash === '#archive' ? 'archive' : 'current', false);
    }

    window.addEventListener('hashchange', syncFromHash);
    syncFromHash();
  })();
</script>

---

> Students are taught minor details in statistics when the hard business of quantitative thinking in economics is getting the data straight; they are taught minor details in mathematics when the hard business of mathematical economics is getting economic ideas straight. (In fact they are often taught mistaken details: that statistical significance, for example, has anything to do with substantive significance; or that a proof on a blackboard is the same thing as a proof in the world [McCloskey 1998; McCloskey and Ziliak 1996]). In most schools they are taught nothing about writing, when the hard business of economic thinking is getting the words straight.
>
> <cite> -- Deirdre N. McCloskey </cite>
