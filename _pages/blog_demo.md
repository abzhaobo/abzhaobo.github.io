---
layout: default
permalink: /blog-demo/
title: Blog 风格示例预览
nav: false
sitemap: false
---

<div class="post">
  <header class="post-header">
    <h1 class="post-title">{{ page.title }}</h1>
    <p class="post-description">
      仅用于预览紧凑 Blog 列表的各类样式组合（支持右上角切换明暗主题查看效果）。不修改任何正式文章，测试后可直接删除本页面。
    </p>
  </header>

  <ul class="post-list post-list-compact">
    <!-- 1. 默认纯文字紧凑样式 -->
    <li class="compact-post-item">
      <div class="compact-post-row">
        <span class="compact-post-date">2026-11-25</span>
        <div class="compact-post-main">
          <a class="compact-post-title" href="{{ '/blog/' | relative_url }}">1. 默认纯文字紧凑样式：人工智能时代的人工</a>
        </div>
        <div class="compact-post-meta">
          <span class="compact-post-readtime">9 min</span>
          <span class="gc-views"><i class="fa-regular fa-eye fa-xs" aria-hidden="true"></i> <span>128</span></span>
        </div>
      </div>
    </li>

    <!-- 2. 右侧小缩略图 -->
    <li class="compact-post-item has-thumb">
      <div class="compact-post-row">
        <span class="compact-post-date">2026-08-10</span>
        <div class="compact-post-main">
          <a class="compact-post-title" href="{{ '/blog/' | relative_url }}">2. 右侧小缩略图（thumbnail）：谈谈“评价”</a>
        </div>
        <div class="compact-post-meta">
          <span class="compact-post-readtime">5 min</span>
          <span class="gc-views"><i class="fa-regular fa-eye fa-xs" aria-hidden="true"></i> <span>94</span></span>
        </div>
        <a class="compact-post-thumb" href="{{ '/blog/' | relative_url }}" aria-hidden="true" tabindex="-1">
          <img src="{{ 'assets/img/HEM.jpg' | relative_url }}" alt="右侧小缩略图示例" loading="lazy">
        </a>
      </div>
    </li>

    <!-- 3. 右侧小缩略图 + 单行摘要 -->
    <li class="compact-post-item has-thumb">
      <div class="compact-post-row">
        <span class="compact-post-date">2026-07-06</span>
        <div class="compact-post-main">
          <a class="compact-post-title" href="{{ '/blog/' | relative_url }}">3. 右侧小图 + 单行摘要（thumbnail + description）：经济学过度模型化</a>
          <div class="compact-post-desc">模型、识别、经验事实和现实语境之间应当如何相互约束？</div>
        </div>
        <div class="compact-post-meta">
          <span class="compact-post-readtime">4 min</span>
          <span class="gc-views"><i class="fa-regular fa-eye fa-xs" aria-hidden="true"></i> <span>215</span></span>
        </div>
        <a class="compact-post-thumb" href="{{ '/blog/' | relative_url }}" aria-hidden="true" tabindex="-1">
          <img src="{{ 'assets/img/hujinquan.jpeg' | relative_url }}" alt="小图加摘要示例" loading="lazy">
        </a>
      </div>
    </li>

    <!-- 4. 柔和渐变背景图条 -->
    <li class="compact-post-item has-bg-img" style="--post-bg-img: url('{{ 'assets/img/quant2026.png' | relative_url }}');">
      <div class="compact-post-row">
        <span class="compact-post-date">2026-06-18</span>
        <div class="compact-post-main">
          <a class="compact-post-title" href="{{ '/blog/' | relative_url }}">4. 柔和渐变背景图条（bg_img）：左侧保留高对比度阅读区，右侧透出图片</a>
        </div>
        <div class="compact-post-meta">
          <span class="compact-post-readtime">12 min</span>
          <span class="gc-views"><i class="fa-regular fa-eye fa-xs" aria-hidden="true"></i> <span>306</span></span>
        </div>
      </div>
    </li>

    <!-- 5. 主题浅背景色高亮 (accent) -->
    <li class="compact-post-item has-bg-color bg-tint-accent">
      <div class="compact-post-row">
        <span class="compact-post-date">2026-06-03</span>
        <div class="compact-post-main">
          <a class="compact-post-title" href="{{ '/blog/' | relative_url }}">5. 主题色浅底高亮（bg_color: accent）：自动随明暗主题切换主色调</a>
        </div>
        <div class="compact-post-meta">
          <span class="compact-post-readtime">5 min</span>
          <span class="gc-views"><i class="fa-regular fa-eye fa-xs" aria-hidden="true"></i> <span>172</span></span>
        </div>
      </div>
    </li>

    <!-- 6a. 暖色背景 (warm) -->
    <li class="compact-post-item has-bg-color bg-tint-warm">
      <div class="compact-post-row">
        <span class="compact-post-date">2026-05-20</span>
        <div class="compact-post-main">
          <a class="compact-post-title" href="{{ '/blog/' | relative_url }}">6a. 暖色浅底（bg_color: warm）：适合随笔、书评或重要置顶提示</a>
        </div>
        <div class="compact-post-meta">
          <span class="compact-post-readtime">6 min</span>
        </div>
      </div>
    </li>

    <!-- 6b. 冷色背景 (cool) -->
    <li class="compact-post-item has-bg-color bg-tint-cool">
      <div class="compact-post-row">
        <span class="compact-post-date">2026-05-12</span>
        <div class="compact-post-main">
          <a class="compact-post-title" href="{{ '/blog/' | relative_url }}">6b. 冷色浅底（bg_color: cool）：适合数据报告、实证分析或技术笔记</a>
        </div>
        <div class="compact-post-meta">
          <span class="compact-post-readtime">8 min</span>
        </div>
      </div>
    </li>

    <!-- 6c. 浅绿背景 (sage) -->
    <li class="compact-post-item has-bg-color bg-tint-sage">
      <div class="compact-post-row">
        <span class="compact-post-date">2026-05-01</span>
        <div class="compact-post-main">
          <a class="compact-post-title" href="{{ '/blog/' | relative_url }}">6c. 浅绿底色（bg_color: sage）：适合教学心得或方法论讨论</a>
        </div>
        <div class="compact-post-meta">
          <span class="compact-post-readtime">4 min</span>
        </div>
      </div>
    </li>

    <!-- 6d. 中性灰背景 (neutral) -->
    <li class="compact-post-item has-bg-color bg-tint-neutral">
      <div class="compact-post-row">
        <span class="compact-post-date">2026-04-18</span>
        <div class="compact-post-main">
          <a class="compact-post-title" href="{{ '/blog/' | relative_url }}">6d. 中性灰底（bg_color: neutral）：低调区分的次级条目</a>
        </div>
        <div class="compact-post-meta">
          <span class="compact-post-readtime">3 min</span>
        </div>
      </div>
    </li>

    <!-- 7. 背景色 + 右侧小图 + 副标题组合 -->
    <li class="compact-post-item has-bg-color bg-tint-warm has-thumb">
      <div class="compact-post-row">
        <span class="compact-post-date">2026-04-02</span>
        <div class="compact-post-main">
          <a class="compact-post-title" href="{{ '/blog/' | relative_url }}">7. 组合样式（bg_color: warm + thumbnail + description）：中国预期寿命数据观察</a>
          <div class="compact-post-desc">可在单篇文章同时叠加底色、右侧缩略图与一行副标题。</div>
        </div>
        <div class="compact-post-meta">
          <span class="compact-post-readtime">7 min</span>
          <span class="gc-views"><i class="fa-regular fa-eye fa-xs" aria-hidden="true"></i> <span>410</span></span>
        </div>
        <a class="compact-post-thumb" href="{{ '/blog/' | relative_url }}" aria-hidden="true" tabindex="-1">
          <img src="{{ 'assets/img/posts/science/life-expectancy.png' | relative_url }}" alt="组合样式示例" loading="lazy">
        </a>
      </div>
    </li>
  </ul>

  <h3>如何在正式文章中启用这些样式？</h3>
  <p>只需在任意 <code>_posts/*.md</code> 顶部的 Frontmatter 中按需添加以下字段即可（不加则为默认纯文字紧凑样式）：</p>

```yaml
---
layout: post
title: 文章标题
date: 2026-11-25
description: 可选的一行简短副标题
thumbnail: assets/img/HEM.jpg        # 可选：右侧小缩略图
bg_img: assets/img/quant2026.png     # 可选：柔和渐变背景图条
bg_color: warm                       # 可选：预设 accent / warm / cool / sage / neutral，或任意 CSS 颜色如 "#f8f5ff"
---
```

  <p class="mt-3">
    <a href="{{ '/blog/' | relative_url }}">&larr; 返回正式 Blog 页面</a>
  </p>
</div>
