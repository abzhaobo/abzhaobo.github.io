---
layout: default
permalink: /blog/
title: Misc 其他
nav: true
nav_order: 3
pagination:
  enabled: true
  collection: posts
  permalink: /page/:num/
  per_page: 25
  sort_field: date
  sort_reverse: true
  trail:
    before: 1 # The number of links before the current page
    after: 3 # The number of links after the current page
---

<div class="post">

<!-- {% assign blog_name_size = site.blog_name | size %}
{% assign blog_description_size = site.blog_description | size %}

{% if blog_name_size > 0 or blog_description_size > 0 %}

  <div class="header-bar">
    <h1>{{ site.blog_name }}</h1>
    <h2>{{ site.blog_description }}</h2>
  </div>
  {% endif %} -->

<div class="header-bar blog-header-bar" style="text-align: left; padding-top: 1rem; padding-bottom: 1.25rem;">
  <div class="row align-items-center">
    <!-- 左侧：专栏标题 -->
    <div class="col-12 col-md-5 text-center text-md-left mb-3 mb-md-0">
      <h1 class="m-0">{{ site.blog_name }}</h1>
    </div>
    <!-- 右侧：胡金铨语录电影截图卡片 -->
    <div class="col-12 col-md-7">
      <div class="text-center text-md-right">
        {% include figure.liquid
           path="assets/img/hujinquan.jpeg"
           class="img-fluid rounded shadow-sm blog-header-quote-img"
           zoomable=true
           alt="胡金铨语录"
        %}
      </div>
    </div>
  </div>
</div>

{% if site.display_tags or site.display_categories %}

  <div class="tag-category-list">
    <ul class="p-0 m-0">
      {% for tag in site.display_tags %}
        <li>
          <i class="fa-solid fa-hashtag fa-sm"></i> <a href="{{ tag | slugify | prepend: '/blog/tag/' | relative_url }}">{{ tag }}</a>
        </li>
        {% unless forloop.last %}
          <p>&bull;</p>
        {% endunless %}
      {% endfor %}
      {% if site.display_categories.size > 0 and site.display_tags.size > 0 %}
        <p>&bull;</p>
      {% endif %}
      {% for category in site.display_categories %}
        <li>
          <i class="fa-solid fa-tag fa-sm"></i> <a href="{{ category | slugify | prepend: '/blog/category/' | relative_url }}">{{ category }}</a>
        </li>
        {% unless forloop.last %}
          <p>&bull;</p>
        {% endunless %}
      {% endfor %}
    </ul>
  </div>
  {% endif %}

{% assign featured_posts = site.posts | where: "featured", "true" %}
{% if featured_posts.size > 0 %}
<br>

<div class="container featured-posts">
{% assign is_even = featured_posts.size | modulo: 2 %}
<div class="row row-cols-{% if featured_posts.size <= 2 or is_even == 0 %}2{% else %}3{% endif %}">
{% for post in featured_posts %}
<div class="card-item col">
<a href="{{ post.url | relative_url }}">
<div class="card hoverable">
<div class="row g-0">
<div class="col-md-12">
<div class="card-body">
<div class="float-right">
<i class="fa-solid fa-thumbtack fa-xs"></i>
</div>
<h3 class="card-title text-lowercase">{{ post.title }}</h3>
<p class="card-text">{{ post.description }}</p>

                    {% if post.external_source == blank %}
                      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
                    {% else %}
                      {% assign read_time = post.feed_content | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
                    {% endif %}
                    {% assign year = post.date | date: "%Y" %}

                    <p class="post-meta">
                      {{ read_time }} min read &nbsp; &middot; &nbsp;
                      <a href="{{ year | prepend: '/blog/' | prepend: site.baseurl}}">
                        <i class="fa-solid fa-calendar fa-sm"></i> {{ year }} </a>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </a>
        </div>
      {% endfor %}
      </div>
    </div>
    <hr>

{% endif %}

  {% comment %}
    Optional per-post frontmatter for compact list styling:
    - thumbnail: assets/img/...   (displays a small thumbnail on the right)
    - bg_img: assets/img/...      (displays a subtle faded background strip)
    - bg_color: warm              (preset: accent/warm/cool/sage/neutral, or any CSS color e.g. "#f8f5ff")
    - description: "..."          (displays an optional single-line subtitle)
  {% endcomment %}
  <ul class="post-list post-list-compact">

    {% if page.pagination.enabled %}
      {% assign postlist = paginator.posts %}
    {% else %}
      {% assign postlist = site.posts %}
    {% endif %}

    {% assign bg_presets = "accent,warm,cool,sage,neutral" | split: "," %}

    {% for post in postlist %}

      {% if post.external_source == blank %}
        {% assign raw_text = post.content | strip_html | strip_newlines %}
      {% else %}
        {% assign raw_text = post.feed_content | strip_html | strip_newlines %}
      {% endif %}
      {% assign char_count = raw_text | remove: ' ' | size %}
      {% assign word_count = raw_text | number_of_words %}
      {% assign word_threshold = word_count | times: 7 %}
      {% if char_count > word_threshold %}
        {% assign read_time = char_count | divided_by: 450 | plus: 1 %}
      {% else %}
        {% assign read_time = word_count | divided_by: 200 | plus: 1 %}
      {% endif %}

      {% assign is_external = false %}
      {% if post.redirect == blank %}
        {% assign post_href = post.url | relative_url %}
      {% elsif post.redirect contains '://' %}
        {% assign post_href = post.redirect %}
        {% assign is_external = true %}
      {% else %}
        {% assign post_href = post.redirect | relative_url %}
      {% endif %}

      {% assign has_bg_color = false %}
      {% assign bg_tint_class = "" %}
      {% assign custom_bg_color = "" %}
      {% if post.bg_color != blank %}
        {% assign has_bg_color = true %}
        {% if bg_presets contains post.bg_color %}
          {% assign bg_tint_class = " bg-tint-" | append: post.bg_color %}
        {% else %}
          {% assign custom_bg_color = post.bg_color %}
        {% endif %}
      {% endif %}

      <li
        class="compact-post-item{% if post.bg_img %} has-bg-img{% endif %}{% if has_bg_color %} has-bg-color{{ bg_tint_class }}{% endif %}{% if post.thumbnail %} has-thumb{% endif %}"
        {% if post.bg_img or custom_bg_color != "" %}
          style="{% if post.bg_img %}--post-bg-img: url('{{ post.bg_img | relative_url }}');{% endif %}{% if custom_bg_color != '' %}--post-bg-color: {{ custom_bg_color }};{% endif %}"
        {% endif %}
      >
        <div class="compact-post-row">
          <span class="compact-post-date">{{ post.date | date: '%Y-%m-%d' }}</span>

          <div class="compact-post-main">
            <a
              class="compact-post-title"
              href="{{ post_href }}"
              {% if is_external %}target="_blank" rel="noopener noreferrer"{% endif %}
            >
              {{- post.title -}}
              {% if is_external %}
                <i class="fa-solid fa-arrow-up-right-from-square fa-2xs compact-post-ext-icon" aria-hidden="true"></i>
              {% endif %}
            </a>
            {% if post.description != blank %}
              <div class="compact-post-desc">{{ post.description }}</div>
            {% endif %}
          </div>

          <div class="compact-post-meta">
            <span class="compact-post-readtime">{{ read_time }} min</span>
            {% if site.enable_goatcounter and site.goatcounter_code and post.redirect == blank %}
              <span class="gc-views" data-gc-path="{{ post.url | relative_url }}" hidden>
                <i class="fa-regular fa-eye fa-xs" aria-hidden="true"></i>
                <span class="gc-count-num"></span>
              </span>
            {% endif %}
          </div>

          {% if post.thumbnail != blank %}
            <a
              class="compact-post-thumb"
              href="{{ post_href }}"
              {% if is_external %}target="_blank" rel="noopener noreferrer"{% endif %}
              aria-hidden="true"
              tabindex="-1"
            >
              <img src="{{ post.thumbnail | relative_url }}" alt="{{ post.title | escape }}" loading="lazy">
            </a>
          {% endif %}
        </div>
      </li>

    {% endfor %}

  </ul>

{% if page.pagination.enabled %}
{% include pagination.liquid %}
{% endif %}

</div>
