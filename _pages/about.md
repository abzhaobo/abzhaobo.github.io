---
layout: about
title: About 介绍
permalink: /
subtitle: "Associate Professor, School of Finance, Nankai University · 南开大学金融学院副教授"

profile:
  align: right
  image: avatar_telaviv.JPG
  image_circular: false # crops the image to make it circular
  more_info: >
    <div class="profile-meta">
      <div class="profile-office"><i class="fa-solid fa-location-dot fa-xs" aria-hidden="true"></i> Room 520, School of Finance</div>
      <div class="profile-links">
        <a href="mailto:zhaobo@nankai.edu.cn" class="profile-pill"><i class="fa-regular fa-envelope fa-xs" aria-hidden="true"></i> Email</a>
        <a href="/assets/pdf/Bo-CV.pdf" class="profile-pill"><i class="fa-regular fa-file-pdf fa-xs" aria-hidden="true"></i> CV</a>
        <a href="https://scholar.google.com/citations?user=_XDNDfEAAAAJ" target="_blank" rel="noopener noreferrer" class="profile-pill"><i class="ai ai-google-scholar" aria-hidden="true"></i> Scholar</a>
      </div>
    </div>

news: true # includes a list of news items
latest_posts: false # includes a list of the newest posts
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false # includes social icons at the bottom of the page
---

Hello! I'm Bo Zhao, an Associate Professor in the School of Finance at Nankai University. My research interests include institutional economics, machine learning, and quantitative investing. I currently teach courses on Quantitative Investment and the History of Economic Methodology. I like basketball and play a little piano.

<ul class="about-edu-list">
  <li><span class="about-edu-year">2016</span><span class="about-edu-detail">PhD in Economics, The University of Hong Kong</span></li>
  <li><span class="about-edu-year">2011</span><span class="about-edu-detail">Master of Financial Engineering, Xiamen University</span></li>
  <li><span class="about-edu-year">2007</span><span class="about-edu-detail">Bachelor of Computational Mathematics, Nanjing University</span></li>
</ul>

<div class="about-bio-zh">
  你好！我是赵博，现任南开大学金融学院副教授。我的研究兴趣包括：制度经济学，机器学习和量化投资。我当前的教学主要包括《量化投资》和《经济分析方法史》。我喜欢打篮球，也弹一点钢琴。
</div>

<div class="about-section research-page">
  <div class="about-section-header">
    <h2 class="about-section-title">Selected Papers</h2>
    <a class="about-section-more" href="{{ '/research/' | relative_url }}">All papers &rarr;</a>
  </div>
  <div class="publications about-selected-papers">
    {% bibliography --group_by none -f working_papers --query @*[selected=true]* %}
    {% bibliography --group_by none -f papers --query @*[selected=true]* %}
  </div>
</div>

<div class="about-recent">
  <div class="about-section-header">
    <h2 class="about-section-title">Selected Writing</h2>
    <a class="about-section-more" href="{{ '/blog/' | relative_url }}">All posts &rarr;</a>
  </div>
  <ul class="post-list post-list-compact about-recent-list">
    {% assign selected_posts = site.posts | where: "selected", true %}
    {% for post in selected_posts %}
      {% assign raw_text = post.content | strip_html | strip_newlines %}
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

      <li class="compact-post-item">
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
        </div>
      </li>
    {% endfor %}
  </ul>
</div>

<div class="about-note-card">
  <div class="about-note-title">The Name Dilemma</div>
  <p>
    In daily life, I go by <em>Bo Zhao</em>. But when publishing academic papers, I use <em>Albert Bo Zhao</em>&mdash;mostly to avoid an identity crisis. You see, the economics and finance world is already packed with heavyweight Bo Zhaos. There's Bo Zhao at the Boston Fed (<a href="https://www.bostonfed.org/people/bank/bo-zhao.aspx">link</a>), Bo Zhao at PKU (<a href="https://en.nsd.pku.edu.cn/faculty/fulltime/z/239574.htm">link</a>), and Bo Zhao at the IMF (<a href="https://development.asia/expert/bo-zhao">link</a>).
  </p>
  <p>
    As a result, I used to get misdirected emails sometimes. So, to make life easier, I publish as Albert Bo Zhao (my friends call me 阿博 (A-Bo)&mdash;so Albert just felt like a natural choice). But don't worry&mdash;if you're emailing me about lunch plans, Bo is just fine.
  </p>
  <p>
    Fun fact: The IMF's Bo Zhao and I not only share the same name but also the same undergraduate alma mater. When we overlapped at HKU, we've joked that we had quite the presence&mdash;at least on paper.
  </p>
</div>
