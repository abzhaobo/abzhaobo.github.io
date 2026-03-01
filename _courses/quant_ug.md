---
layout: page
title: 人工智能时代的量化投资(本科，2026)
description: 因子模型；技术分析的统计检验；机器学习
img: assets/img/quant2025.png
importance: 1
category: 2026
giscus_comments: true
numbering: true
toc: 
  sidebar: left
no_number: ["通知"]
---

## ❗️通知 Announcement❗️

## 课程大纲 Syllabus

<!-- <details markdown="1">
  <summary> 详细内容 </summary> -->

### 课程简介

《人工智能时代的量化投资》是一门面向本科生的应用导向课程，系统介绍如何使用数量方法、计算机编程和现代数据分析工具分析金融市场数据，并构建可检验、可复现的投资与交易策略。

本课程在内容架构上与研究生层面的《量化投资》类似，但对于具体细节的深度要求会相对低一些。研究生的课程自2020年起即包含机器学习和深度学习的内容。今年的课程将在讲解清楚原理的基础上，进一步探讨AI相关内容的应用。具体内容将根据实际进度和大家的作业完成情况进行调整。

### 课程目标

通过本课程的学习，学生应当能够：

- 熟练使用 Python 及常用数据分析与机器学习工具处理金融数据；
- 理解常见量化投资模型与策略背后的基本思想和适用条件；
- 独立完成从数据处理、特征构建到策略回测与评估的完整流程；
- 对量化方法的优势、局限性及潜在风险形成基本判断。

### 主要内容

课程内容是应用导向的，但相关的理论也会有涉及。课程目标：掌握基本的工具以及用数据分析的思维方式。这门课主要包含以下内容：
- Python 基础以及数据处理相关库(numpy, pandas, SKlearn, Pytorch等)
- 回测框架
- 因子模型以及统计检验
- 技术分析介绍以及统计检验
- 机器学习和深度学习在量化投资中的应用
- 多工具综合应用

本课程不涉及高频（日内）交易策略。主要数据来源为中国 A 股市场。

### 知识储备 

学生应具备基本的概率论、统计学和计量经济学知识。课程不要求学生事先具备编程经验，所有与 Python 编程和数据分析相关的内容都会在课程中系统讲解；但需要做好进行较多编程练习和上机操作的心理准备。

---

### 教材与参考书

我们采用的量化回测平台是[优矿](https://uqer.datayes.com/)，请至相关网页下载客户端。优矿有免费版但分配的计算资源很少，学院会提供一些共享账号。参考书目见下方。本课程不设指定教材。课程讲义、代码示例及相关资料将统一上传至本网页，请同学在每次上课前自行下载最新版本。

主要参考书目包括（但不限于）：

- Cochrane, J. H. (2005). *Asset Pricing*. Princeton University Press.
- Bali, T. G., Engle, R. F., & Murray, S. (2016). *Empirical Asset Pricing*. Wiley.
- 石川、刘洋溢、连祥斌 (2020). 《因子投资：方法与实践》. 电子工业出版社.
- Murphy, J. J. (1999). *Technical Analysis of the Financial Markets*. New York Institute of Finance.
- Grinold, R., & Kahn, R. (1999). *Active Portfolio Management*. McGraw-Hill.
- Géron, A. (2021). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly.

---

### 评分方式

- 3次作业（70%）
- 闭卷考试 (30%)

闭卷考试形式：闭卷考试客观题占30%--40%，主观设计题占60%--70%。不考察死记硬背的代码语法或API参数，旨在考察学生对于重要概念的理解，以及是否有正确的思路构建、查验量化项目。

本课程鼓励使用AI进行编程，但**严禁抄袭、复制他人作业。** 一经发现，将按照学校相关规定严肃处理，可能会直接挂科。对编程经验较少的同学而言，学习过程中遇到困难是正常的；课程将提供示例代码和必要的指导，只要认真完成练习，即可顺利完成课程要求。

<!-- </details> -->

&nbsp;

## 课程内容 Contents

<table class="course-table">
  <thead>
    <tr>
      <th>课次</th>
      <th>日期</th>
      <th>内容</th>
      <th>课件与资料</th>
      <th>参考文献</th>
      <th>作业</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td>1</td>
    <td>3月2日</td>
    <td>
    1. 方法论简介 <br>
    2. Python基础与环境配置
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>2</td>
    <td>3月9日</td>
    <td>
    Python进阶与金融数据处理
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>3月16日</td>
    <td>
    量化平台（优矿）介绍与回测代码构建
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>4</td>
    <td>3月23日</td>
    <td>
    探索性数据分析
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>5</td>
    <td>3月30日</td>
    <td>
    因子模型的技术和思想
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>6</td>
    <td>4月6日</td>
    <td>
    单因子模型（CAPM，Beta因子）
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>7</td>
    <td>4月13日</td>
    <td>
    异象与排序法实证：市值因子与价值因子
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>8</td>
    <td>4月20日</td>
    <td>
    多因子模型：Fama-French 三因子模型理论与实现
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>9</td>
    <td>4月27日</td>
    <td>
    经典因子拓展：动量、反转、流动性与波动率
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>10</td>
    <td>5月4日</td>
    <td>
    因子模型的量化策略回测框架与绩效评估指标
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>11</td>
    <td>5月11日</td>
    <td>
    技术分析的技术准备：Bootstrap检验
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>12</td>
    <td>5月18日</td>
    <td>
    择时策略与技术指标的实证分析和量化检验
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>13</td>
    <td>5月25日</td>
    <td>
    选股和择时的综合应用
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>14</td>
    <td>6月1日</td>
    <td>
    机器学习基础
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>15</td>
    <td>6月8日</td>
    <td>
    实践导向的机器学习
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>16</td>
    <td>6月15日</td>
    <td>
    综合案例：机器学习视角下中国股票收益率可预测性分析
    </td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  </tbody>
</table>



-----
[Back to top](#)