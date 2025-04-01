---
layout: page
title: 量化投资/金融数据分析 Quantitative Investment (2022)
description: Factor models, empirical tests of technical analysis indicators, applications of machine learning techniques
img: assets/img/quant2022.png
importance: 3
category: Earlier
---
- [❗️通知 Announcement❗️](#️通知-announcement️)
- [1. 课程大纲 Syllabus](#1-课程大纲-syllabus)
  - [1.1 知识储备 Prerequisites](#11-知识储备-prerequisites)
  - [1.2 课本和参考书 Textbook and References](#12-课本和参考书-textbook-and-references)
  - [1.3 评分方式 Grading](#13-评分方式-grading)
- [2. 课件 Materials](#2-课件-materials)
  - [Lecture 1. Introduction to Python](#lecture-1-introduction-to-python)
  - [Lecture 2. Introduction to Data Science Packages and Uqer Platform](#lecture-2-introduction-to-data-science-packages-and-uqer-platform)
  - [Lecture 3. Exploratory Data Analysis \& Introduction to Factor Models](#lecture-3-exploratory-data-analysis--introduction-to-factor-models)
  - [Lecture 4. Sorting, Fama-MacBeth Regression, Fama French 3 Factors](#lecture-4-sorting-fama-macbeth-regression-fama-french-3-factors)
  - [Lecture 5. Momentum, Reversal, Liquidity, Volatility Factors.](#lecture-5-momentum-reversal-liquidity-volatility-factors)
  - [Lecture 6. Applications of Factor Models. Introduction to Technical Analysis and Related Econometrics](#lecture-6-applications-of-factor-models-introduction-to-technical-analysis-and-related-econometrics)
  - [Lecture 7. Statistical Tests of Technical Indicators. Introduction to Machine Learning Methods](#lecture-7-statistical-tests-of-technical-indicators-introduction-to-machine-learning-methods)
  - [Lecture 8. Applications of Machine Learning to Factor Models and Technical Analysis](#lecture-8-applications-of-machine-learning-to-factor-models-and-technical-analysis)
- [致谢](#致谢)

# ❗️通知 Announcement❗️

2022.04.24 讲座：戴嵩 长江养老保险基金经理。腾讯会议号：902 133 587

2022.04.05 清明节放假，停课一次。

2022.03.30 (递交截止时间：2022.04.13 上午12:00): 作业3：[ex3.pdf](/assets/courses/quant/exercises/ex3.pdf)

2022.03.09 (递交截止时间：2022.03.23 上午12:00): 作业2：[ex2.pdf](/assets/courses/quant/exercises/ex2.pdf)

2022.02.23 (递交截止时间：2022.03.09 上午12:00): 作业1：[ex1.pdf](/assets/courses/quant/exercises/ex1.pdf)，[stk_df_21_22.zip](/assets/courses/quant/ex1/stk_df_21_22.zip)

# 1. 课程大纲 Syllabus

这门课程在教学计划上有两个不同的名称：《量化投资》(学硕)，《金融数据分析和Python应用》(专硕)。主要讨论用数量方法探索金融数据以及构建交易策略。课程内容是应用导向的，但相关的理论也会有涉及。其目的是让学生学会基本的工具、掌握量化的思维方式，为今后的职业生涯打下基础。这门课主要包含以下内容：
- Python 基础以及数据处理相关库(numpy, pandas, sklearn, tensorflow, keras等)
- 因子模型构建
- 技术分析简介
- 机器学习在量化投资中的应用

一些内容(例如机器学习的应用)仍在不断地发展之中，课程内容仍可能根据实际情况进行调整。

<!-- 这门课暂不包含高频数据(日内)策略，也不包含衍生品策略。主要的数据来源是中国A股市场股票数据 -->

This is a course about constructing trading strategies by quantitative methods. The course is application oriented, but relevant theories will also be discussed. The course objective is to teach students basic tools and ways of exploring financial data so that quantitative (and perhaps winning) strategies can be constructed. The main contents are:
- introduction of Python basics and data science packages (numpy, pandas, sklearn, tensorflow, keras, etc.)
- construction of factor models
- introduction to technical analysis
- application of machine learning methods

Some of the above mentioned fields are fast developing (e.g. machine learning applications), and thus the contents may be subject to change.

<!-- This course does not contain high-frequency (intraday) strategies, or strategies involving derivatives (yet). Please refer to other courses provided by the department if these are what you need. Our main data is from A shares of China's stock markets. -->

## 1.1 知识储备 Prerequisites
应当知道基本的计量经济学(如需要我们可进行简短的复习)。无需具备编程知识，所有的编程相关的内容都会在课程中介绍(若有编程经验当然更好)。但面对大量的编程应当有心理准备。

Students should know basic econometrics (I'll give short review lectures if necessary). Students must also be comfortable, or inclined to do lots of programming. No prior knowledge of programming is required, though it is surely a big plus if you have some experiences.

## 1.2 课本和参考书 Textbook and References
暂无课本。课件和相关资料会上传到这个网页，请每次上课前进行下载。我们采用的平台是[优矿](https://uqer.datayes.com/)，请至相关网页下载客户端。优矿有免费版但分配的计算资源很少，学院会提供一些共享账号。参考书目见下方。

There is no required textbook. Lecture notes will be uploaded here and please download the latest version before class. We'll be using [Uqer](https://uqer.datayes.com/), a quant platform, for retrieving data, programming and backtesting. Please download and install it on your laptop. The platform is not free, but we'll give you several shared accounts.

The following references are useful:
- Cochrane, John H., 2005, *Asset Pricing*. Revised edition. (Princeton University Press, Princeton, N.J).
- Bali, Turan G., Robert F. Engle, and Scott Murray, 2016, *Empirical Asset Pricing: The Cross Section of Stock Returns*. 1 edition. (Wiley).
- Murphy, John J., 1999, *Technical Analysis of the Financial Markets: A Comprehensive Guide to Trading Methods and Applications*. (New York Institute of Finance, N.Y.).
- Grinold, Richard, and Ronald Kahn, 1999, *Active Portfolio Management: A Quantitative Approach for Producing Superior Returns and Controlling Risk*. 2 edition. (McGraw-Hill Education, New York).
- Geron, Aurelien, 2019, *Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow*. 2nd Edition (O'Reilly).

## 1.3 评分方式 Grading
(暂定，可能会有所改动)
- 3到4次作业 (60%)
- 家庭考试 (40%)

(preliminary, may be subject to changes)
- 3 or 4 homework exercises (60%)
- take-home exam (40%)

**抄袭作业零容忍。抄袭他人作业可能会直接挂科。** 对于编程经验较少的同学来说，遇到困难是正常的。所有的代码我都会共享，只要仔细研读一定可以完成作业和考试。请相信自己。

**PLAGIARISM IS STRICTLY PROHIBITED. You may immediately fail the course if copy-pasting other's work.** It will be normal to meet obstacles during the course, especially for students with less exposure to programming. I'll share all relevant codes and you'll surely complete the course successfully if you read and try the provided codes with some care. Please trust yourself and hang on.

# 2. 课件 Materials
## Lecture 1. Introduction to Python
[lec-1.pdf](/assets/courses/quant/lec1/lec-1.pdf)

[Python_intro.ipynb](/assets/courses/quant/lec1/Python_intro.ipynb)

[Python_intro.html](/assets/courses/quant/lec1/Python_intro.html)

## Lecture 2. Introduction to Data Science Packages and Uqer Platform

numpy, pandas, plottting introduction: [np_pd_plot.ipynb](/assets/courses/quant/lec2/np_pd_plot.ipynb), [np_pd_plot.html](/assets/courses/quant/lec2/np_pd_plot.html)

Uqer strategy example: [strategy_example_202202.ipynb](/assets/courses/quant/lec2/strategy_example_202202.ipynb)，[strategy_example_202202.html](/assets/courses/quant/lec2/strategy_example_202202.html)，[优矿量化投资策略教程示例文件](/assets/courses/quant/lec2/量化投资策略教程示例文件.nb)

## Lecture 3. Exploratory Data Analysis & Introduction to Factor Models

Quick review of robust errors: [crash_note.pdf](/assets/courses/quant/lec3/crash_note.pdf)

Fundamental econometrics related to factor models: [econometrics_summary.ipynb](/assets/courses/quant/lec3/econometrics_summary.ipynb), [econometrics_summary.pdf](/assets/courses/quant/lec3/econometrics_summary.pdf)

Exploratory Data Analysis: [1-EDA.ipynb](/assets/courses/quant/lec3/1-EDA.ipynb), [1-EDA.html](/assets/courses/quant/lec3/1-EDA.html)

## Lecture 4. Sorting, Fama-MacBeth Regression, Fama French 3 Factors

(Updated on 2022.03.15) Sorting and FM regression on beta, size: [2-sort_FMreg_on_beta_size.ipynb](/assets/courses/quant/lec4/2-sort_FMreg_on_beta_size.ipynb), [2-sort_FMreg_on_beta_size.html](/assets/courses/quant/lec4/2-sort_FMreg_on_beta_size.html)

(Updated on 2022.03.15) Fama-French 3 factors: [3-FF3.ipynb](/assets/courses/quant/lec4/3-FF3.ipynb), [3-FF3.html](/assets/courses/quant/lec4/3-FF3.html)

## Lecture 5. Momentum, Reversal, Liquidity, Volatility Factors.

Momentum and reversal: [4-momentum_reversal.ipynb](/assets/courses/quant/lec5/4-momentum_reversal.ipynb), [4-momentum_reversal.html](/assets/courses/quant/lec5/4-momentum_reversal.html)

Wrapping code for creating factors: [factors.ipynb](/assets/courses/quant/lec5/factors.ipynb), [factors.html](/assets/courses/quant/lec5/factors.html)

(Updated on 2022.03.22) Liquidity and volatility: [5-liquidity_volatility.ipynb](/assets/courses/quant/lec5/5-liquidity_volatility.ipynb), [5-liquidity_volatility.html](/assets/courses/quant/lec5/5-liquidity_volatility.html)

Code used in "myutils": [code_in_myutils.zip](/assets/courses/quant/lec5/code_in_myutils.zip)

## Lecture 6. Applications of Factor Models. Introduction to Technical Analysis and Related Econometrics

(updated 2022.03.23) Applications of factor models: [6-factor_application.ipynb](/assets/courses/quant/lec6/6-factor_application.ipynb), [6-factor_application.html](/assets/courses/quant/lec6/6-factor_application.html)

(updated 2022.03.23) Backtesting with uqer, cross sectional selection of stocks: [6-backtest.ipynb](/assets/courses/quant/lec6/6-backtest.ipynb)

(updated 2022.03.29)Ideas of Technical Analysis: [技术分析的基本思想和统计检验.pdf](/assets/courses/quant/lec6/技术分析的基本思想和统计检验.pdf)

## Lecture 7. Statistical Tests of Technical Indicators. Introduction to Machine Learning Methods

Bootstrap review: [bootstrap.R](/assets/courses/quant/lec7/bootstrap.R), [bootstrapping.pdf](/assets/courses/quant/lec7/bootstrapping.pdf)

(updated 2022.03.29)Statistical tests of technical indicators: [7-ta_test.ipynb](/assets/courses/quant/lec7/7-ta_test.ipynb), [7-ta_test.html](/assets/courses/quant/lec7/7-ta_test.html)

Backtests with both stock-picking and market timing: [7-crs_and_timing.ipynb](/assets/courses/quant/lec7/7-crs_and_timing.ipynb)


## Lecture 8. Applications of Machine Learning to Factor Models and Technical Analysis

[Gu et al. (2020)](/assets/courses/quant/lec8/Gu-2020.pdf)

[Wu et al. (2019)](/assets/courses/quant/lec8/Wu-2019.pdf)

[Leippold et al. (2021)](/assets/courses/quant/lec8/Leippold-2021.pdf)

Machine learning applications in factor models: [8-factor_ML.ipynb](/assets/courses/quant/lec8/8-factor_ML.ipynb), [8-factor_ML.html](/assets/courses/quant/lec8/8-factor_ML.html)

Machine learning applications in technical analysis: [8-ta_ML.ipynb](/assets/courses/quant/lec8/8-ta_ML.ipynb), [8-ta_ML.html](/assets/courses/quant/lec8/8-ta_ML.html)

# 致谢

这门课是南开大学“智能投顾虚拟教研室”的线上公开课之一。感谢南开大学金融学院领导、刘澜飚教授和周爱民教授的大力支持！感谢[优矿](https://uqer.datayes.com/)、[同花顺](https://www.10jqka.com.cn/)、[悟空投资](https://www.wukongtz.com/)对虚拟教研室以及本课程的大力支持！

-----
[Back to top](#)