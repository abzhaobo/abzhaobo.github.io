---
layout: page
title: 量化投资/金融数据分析 Quantitative Investment (2024)
description: Factor models, empirical tests of technical analysis indicators, applications of machine learning techniques
img: assets/img/quant.png
importance: 1
category: Quant
---

- [❗️通知 Announcement❗️](#️通知-announcement️)
- [1. 课程大纲 Syllabus](#1-课程大纲-syllabus)
  - [1.1 知识储备 Prerequisites](#11-知识储备-prerequisites)
  - [1.2 课本和参考书 Textbook and References](#12-课本和参考书-textbook-and-references)
  - [1.3 评分方式 Grading](#13-评分方式-grading)
- [2. 课程内容 Contents](#2-课程内容-contents)

# ❗️通知 Announcement❗️


# 1. 课程大纲 Syllabus

<!-- &nbsp; -->

<details markdown="1">
  <summary> 详细内容 Details </summary>

这门课程在教学计划上有两个不同的名称：《量化投资》(学硕)，《金融数据分析和Python应用》(专硕)。主要讨论用数量方法探索金融数据以及构建交易策略。课程内容是应用导向的，但相关的理论也会有涉及。课程目标：掌握基本的工具以及用数据分析的思维方式。这门课主要包含以下内容：
- Python 基础以及数据处理相关库(numpy, pandas, sklearn, tensorflow, keras等)
- 因子模型
- 技术分析介绍以及统计检验
- 机器学习在量化投资中的应用

这门课暂不包含高频数据(日内)策略，也不包含衍生品策略。主要的数据来源是中国A股市场股票数据

This is a course about constructing trading strategies by quantitative methods. The course is application oriented, but relevant theories will also be discussed. The course objective is to teach students basic tools and ways of exploring financial data so that quantitative (and perhaps winning) strategies can be constructed. The main contents are:
- introduction of Python basics and data science packages (numpy, pandas, sklearn, tensorflow, keras, etc.)
- construction of factor models
- introduction to technical analysis
- application of machine learning methods

This course does not contain high-frequency (intraday) strategies, or strategies involving derivatives. Please refer to other courses provided by the school if these are what you need. Our main data is from A shares of China's stock markets.


## 1.1 知识储备 Prerequisites
应当知道基本的计量经济学(我们会进行简短的复习)。无需具备编程知识，所有的编程相关的内容都会在课程中介绍，但如果有编程经验更好。面对大量的编程应当有心理准备。

Students should know basic econometrics (I'll give short review lectures if necessary). Students must also be comfortable, or inclined to do lots of programming. No prior knowledge of programming is required, though it is surely a big plus if you have some experiences.

## 1.2 课本和参考书 Textbook and References
暂无课本。课件和相关资料会上传到这个网页，请每次上课前进行下载。我们采用的平台是[优矿](https://uqer.datayes.com/)，请至相关网页下载客户端。优矿有免费版但分配的计算资源很少，学院会提供一些共享账号。参考书目见下方。

There is no required textbook. Lecture notes will be uploaded here and please download the latest version before class. We'll be using [Uqer](https://uqer.datayes.com/), a quant platform, for retrieving data, programming and backtesting. Please download and install it on your laptop. The platform is not free, but we'll give you several shared accounts.

The following references are useful:
- Cochrane, John H., 2005, *Asset Pricing*. Revised edition. (Princeton University Press, Princeton, N.J).
- Bali, Turan G., Robert F. Engle, and Scott Murray, 2016, *Empirical Asset Pricing: The Cross Section of Stock Returns*. 1 edition. (Wiley).
- 石川, 刘洋溢, & 连祥斌. (2020). 因子投资：方法与实践. 电子工业出版社.
- Murphy, John J., 1999, *Technical Analysis of the Financial Markets: A Comprehensive Guide to Trading Methods and Applications*. (New York Institute of Finance, N.Y.).
- Grinold, Richard, and Ronald Kahn, 1999, *Active Portfolio Management: A Quantitative Approach for Producing Superior Returns and Controlling Risk*. 2 edition. (McGraw-Hill Education, New York).
- Geron, Aurelien, 2021, *Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow*. 3rd Edition (O'Reilly).

## 1.3 评分方式 Grading
(暂定，可能会有所改动)
- 3到4次作业 (60%)
- 家庭考试 (40%)。大致形式为在规定时间内完成策略构建。

(preliminary, may be subject to changes)
- 3 or 4 homework exercises (60%)
- take-home exam (40%)

**抄袭作业零容忍。抄袭他人作业可能会直接挂科。** 对于编程经验较少的同学来说，遇到困难是正常的。所有的代码我都会共享，只要仔细研读一定可以完成作业和考试。请相信自己。

**PLAGIARISM IS STRICTLY PROHIBITED. You may immediately fail the course if copy-pasting other's work.** It will be normal to meet obstacles during the course, especially for students with less exposure to programming. I'll share all relevant codes and you'll surely complete the course successfully if you read and try the provided codes with some care. Please trust yourself and hang on.

</details>

&nbsp;

# 2. 课程内容 Contents



-----
[Back to top](#)