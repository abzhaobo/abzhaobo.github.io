---
layout: page
title: 中级计量经济学 Intermediate Econometrics
description: Methods in identifying (causal) relationships in social science
img: assets/img/econometrics.jpeg
importance: 4
category: Earlier
giscus_comments: false
---
- [❗️Announcement❗️](#️announcement️)
- [Syllabus](#syllabus)
  - [Text Book and Useful References](#text-book-and-useful-references)
  - [Grading](#grading)
- [Materials](#materials)
  - [Lecture 0. Introduction](#lecture-0-introduction)
  - [Lecture 1. Finite Sample OLS](#lecture-1-finite-sample-ols)
  - [Lecture 2. Large Sample Theory](#lecture-2-large-sample-theory)
  - [Lecture 3. Heteroskedasticity, Autocorrelation and Generalized Least Squares](#lecture-3-heteroskedasticity-autocorrelation-and-generalized-least-squares)
  - [Lecture 4. Maximum Likelihood Estimation](#lecture-4-maximum-likelihood-estimation)
  - [Lecture 5. Specification Error, Measurement Error, and other Data Problems](#lecture-5-specification-error-measurement-error-and-other-data-problems)
  - [Lecture 6. Instrumental Variable and Generalized Methods of Moments](#lecture-6-instrumental-variable-and-generalized-methods-of-moments)
  - [Lecture 7. Simultaneous Equations Model, Panel Regressions](#lecture-7-simultaneous-equations-model-panel-regressions)
  - [Lecture 8. Dynamic Panel Regressions](#lecture-8-dynamic-panel-regressions)
  - [Lecture 9. Monte Carlo Methods and Bootstrap](#lecture-9-monte-carlo-methods-and-bootstrap)
  - [Lecture 10. Random Experiments and Natural Experiments, Treatment Effects](#lecture-10-random-experiments-and-natural-experiments-treatment-effects)
  - [Lecture 11. Time Series Models](#lecture-11-time-series-models)
  - [Lecture 12. Machine Learning and Econometrics](#lecture-12-machine-learning-and-econometrics)

# ❗️Announcement❗️

2021.12.10: [2020考试题](/assets/courses/econometrics/2020-final.pdf)

2021.12.03: [作业4](/assets/courses/econometrics/ex4/ex4.pdf). [数据](/assets/courses/econometrics/ex4/ex4_data.zip). 参考答案：[RDD](/assets/courses/econometrics/ex4/rdd.pdf), [Housing](/assets/courses/econometrics/ex4/housing-example.html)

2021.11.12: 请确认复制论文选题后在此列表中登记选题：[复制论文列表](https://docs.qq.com/sheet/DRWFnYWdGblFLbVVy).

2021.11.12: [作业3](/assets/courses/econometrics/ex3/ex3.pdf). [作业3参考解答](/assets/courses/econometrics/ex3/sol3.pdf)

2021.10.22: [作业2](/assets/courses/econometrics/ex2/ex2.pdf). [数据](/assets/courses/econometrics/ex2/BWGHT.DTA). [作业2参考解答](/assets/courses/econometrics/ex2/sol2.pdf)

2021.10.08: [作业1](/assets/courses/econometrics/ex1/ex1.pdf). [参考解答](/assets/courses/econometrics/ex1/solution1.pdf)

# Syllabus

This course is an applied econometrics course, in the sense that mathematical details are less emphasized. That being said, students are expected to know undergraduate level linear algebra, calculus, probability and statistics. The main contents are:

- Finite Sample OLS
- Large Sample Theory
- Maximum Likelihood Estimation
- Endogeneity Problems in Economics
- Instrumental Variables and Generalized Methods of Moments
- Panel Regressions
- Random Experiments and Natural Experiments
- Treatment Effects

If time permits, we'll also briefly discuss the following topics: simultaneous equations models, binary-response models, machine learning fundamentals. The goal is to let students know both the big picture and necessary details of applying statistical (including econometrics and machine learning) models to problems in social sciences, especially economics and finance.

这门课是 **应用** 计量经济学。因此，除了关键步骤，数学推导将尽量减少。但微积分、线性代数、概率论和统计的主要知识仍然必不可少。主要内容如下：

- 小样本OLS及其性质
- 大样本OLS
- 最大似然估计
- 内生性问题的几种来源
- 工具变量，GMM
- 面板回归
- 蒙特卡洛模拟和自助法
- 随机实验和自然实验
- 处理效应

如果时间允许，我们也会简要讨论以下一些内容：联立方程模型，二值选择模型，机器学习基础。讨论这些内容的原因：让学生对社会科学研究中的问题的性质，以及如何根据这些性质选择合适的数量模型，有比较明确的认识。

## Text Book and Useful References

Text book: 陈强, 《高级计量经济学及Stata应用》，第2版，[http://www.econometrics-stata.com/col.jsp?id=101](http://www.econometrics-stata.com/col.jsp?id=101)

References:
- Hayashi, F. (2000). Econometrics. Princeton University Press.
- Wooldridge, J. M. (2010). Econometric Analysis of Cross Section and Panel Data, 2nd ed.
- Angrist, J. D., and J. Pischke, 2009, Mostly Harmless Econometrics: An Empiricist's Companion. 1 edition. (Princeton University Press).

## Grading
- 3 to 4 exercises, 20%
- Replication project, 40%. [Requirement](/assets/courses/econometrics/replication_project.pdf)
- Final exam, 40%


**PLAGIARISM IS STRICTLY PROHIBITED. You may immediately fail the course if copy-pasting other's work.** Discussion is, of course, permitted.

**抄袭作业零容忍。抄袭他人作业可能会直接挂科。** 讨论、交流没有问题，但仍需自己完成。

# Materials

## Lecture 0. Introduction
[Slides](/assets/courses/econometrics/1-介绍-2021.pdf)

## Lecture 1. Finite Sample OLS
[Slides](/assets/courses/econometrics/1-绪论-小样本OLS.pdf)

[annotated slides](/assets/courses/econometrics/annotated-slides.7z)

[hand-written notes](/assets/courses/econometrics/notes/20210924-lec-notes.7z)

## Lecture 2. Large Sample Theory
[Slides](/assets/courses/econometrics/2-大样本OLS.pdf)

[annotated slides](/assets/courses/econometrics/anno-2-大样本OLS.pdf)

## Lecture 3. Heteroskedasticity, Autocorrelation and Generalized Least Squares
[Slides](/assets/courses/econometrics/3-第7,8章-异方差与GLS-自相关.pdf)

[annotated slides](/assets/courses/econometrics/anno-3-第7,8章-异方差与GLS-自相关.pdf)

[Newey-West estimator](/assets/courses/econometrics/notes/NW.pdf)

## Lecture 4. Maximum Likelihood Estimation
[Slides](/assets/courses/econometrics/4-最大似然估计.pdf)

[annotated slides](/assets/courses/econometrics/anno-4-最大似然估计.pdf)

[hand-written notes of Lec 4 and 5, Oct.15](/assets/courses/econometrics/notes/10.15.zip)

## Lecture 5. Specification Error, Measurement Error, and other Data Problems
[Slides](/assets/courses/econometrics/5-第9章-模型设定与数据问题.pdf)

[annotated slides, Oct.22 updated](/assets/courses/econometrics/anno-5-第9章-模型设定与数据问题.pdf)

## Lecture 6. Instrumental Variable and Generalized Methods of Moments
[Slides](/assets/courses/econometrics/6-第10章-工具变量法，2SLS与GMM.pdf)

[annotated slides, Nov.6 updated](/assets/courses/econometrics/anno-6-第10章-工具变量法，2SLS与GMM.pdf)


[hand-written notes, Oct.22](/assets/courses/econometrics/notes/10.22.zip)

[Efficiency of 2SLS vs. IV when homoskedasticity](/assets/courses/econometrics/notes/efficiency-2SLS_vs_IV.pdf)

## Lecture 7. Simultaneous Equations Model, Panel Regressions

[SEM Slides](/assets/courses/econometrics/7-SEM.pdf)

[annotated slides, Nov.6](/assets/courses/econometrics/anno-7-SEM.pdf)

[hand-written notes, Nov.5](/assets/courses/econometrics/notes/11.5.zip)

[Panel Slides](/assets/courses/econometrics/7-第15章-短面板.pdf)

[Annotated Panel Slides, Nov.12 updated](/assets/courses/econometrics/anno-7-第15章-短面板.pdf)

## Lecture 8. Dynamic Panel Regressions
[Slides](/assets/courses/econometrics/8-第16章-长面板与动态面板.pdf)

[annotated slides, Nov.12](/assets/courses/econometrics/anno-8-第16章-长面板与动态面板.pdf)

[hand-written notes, Nov.12](/assets/courses/econometrics/notes/11.12.zip)

## Lecture 9. Monte Carlo Methods and Bootstrap
[Slides](/assets/courses/econometrics/9-第19章-蒙特卡罗法与自助法.pdf)

[annotated slides, Monte Carlo and Bootstrap, Nov.19](/assets/courses/econometrics/anno-9-第19章-蒙特卡罗法与自助法.pdf)

[Example](/assets/courses/econometrics/9-MonteCarloExample.html)

[R code](/assets/courses/econometrics/9-MonteCarloExample.R)


## Lecture 10. Random Experiments and Natural Experiments, Treatment Effects
[1. Experiments Slides](/assets/courses/econometrics/10-第18章-随机实验与自然实验.pdf)

[1. annotated Experiments Slides, Nov.19](/assets/courses/econometrics/anno-10-第18章-随机实验与自然实验.pdf)

[2. Binary Choice Models Slides](/assets/courses/econometrics/11-第11章-二值选择模型.pdf)

[2. annotated Binary Choice Models Slides, Nov.19](/assets/courses/econometrics/anno-11-第11章-二值选择模型.pdf)

[hand-written notes, Nov.19](/assets/courses/econometrics/notes/11.19.zip)

[3. Treatment Effects Slides](/assets/courses/econometrics/11-第28章-处理效应.pdf)

[annotated 3. Treatment Effects Slides](/assets/courses/econometrics/anno-11-第28章-处理效应.pdf)
## Lecture 11. Time Series Models
[1. Stationary process](/assets/courses/econometrics/12-第20章-平稳时间序列.pdf)

[1. Annotated Stationary process](/assets/courses/econometrics/anno-12-第20章-平稳时间序列.pdf)

[hand-written notes, Nov.26](/assets/courses/econometrics/notes/11.26.pdf)

[2. Unit root and cointegration](/assets/courses/econometrics/12-第21章-单位根与协整.pdf)

[2. annotated unit root and cointegration](/assets/courses/econometrics/anno-12-第21章-单位根与协整.pdf)

[3. GARCH](/assets/courses/econometrics/12-第22章-自回归条件异方差模型.pdf)

[3. annotated GARCH](/assets/courses/econometrics/anno-12-第22章-自回归条件异方差模型.pdf)

[An ARIMA forecast example](/assets/courses/econometrics/arima_forecast.7z)

## Lecture 12. Machine Learning and Econometrics
[Machine Learning Slides](/assets/courses/econometrics/ML.pdf)

[entropy](/assets/courses/econometrics/notes/entropy.pdf)

The book I mentioned in class for learning ML (strongly recommend): <https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/>. The author provides complete hands-on code here: <https://github.com/ageron/handson-ml2>

Classical references on the statistical models: [An Introduction to Statistical Learning](https://www.statlearning.com/), [The Elements of Statistical Learning](https://www.amazon.com/Elements-Statistical-Learning-Prediction-Statistics/dp/0387848576). 中文参考书：[西瓜书](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/MLbook2016.htm)

-----
[Back to top](#)