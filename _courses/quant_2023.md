---
layout: page
title: 量化投资/金融数据分析 Quantitative Investment (2023)
description: Factor models, empirical tests of technical analysis indicators, applications of machine learning techniques
img: assets/img/quant.png
importance: 3
category: Quant
---

- [❗️通知 Announcement❗️](#️通知-announcement️)
- [1. 课程大纲 Syllabus](#1-课程大纲-syllabus)
  - [1.1 知识储备 Prerequisites](#11-知识储备-prerequisites)
  - [1.2 课本和参考书 Textbook and References](#12-课本和参考书-textbook-and-references)
  - [1.3 评分方式 Grading](#13-评分方式-grading)
- [2. 课程内容 Contents](#2-课程内容-contents)

# ❗️通知 Announcement❗️

- 🎉🎉 5月9日: 感谢各位同学的课程评价！

    [课程评价部分统计报告](/assets/courses/quant_2023/report.pdf)（截止至2023年5月9日）

    <!-- [课程评价原始数据.csv](/assets/courses/quant_2023/evaluation_data.csv) -->
- 4月12日: 考试题已布置。请于4月26日中午12点前提交。考题：[exam.pdf](/assets/courses/quant_2023/exam.pdf)。数据：[data.zip](https://share.weiyun.com/L6hnDxYt)
- 3月21日: 作业3已布置。请于4月05日中午12点前提交。
- 量化投研实践讲座。时间：3月29日18:30。嘉宾：孙子文, 国联证券研究所量化研究员。腾讯会议号：579-655-025
- 3月07日: 作业2已布置。请于3月22日中午12点前提交。
- 2月22日: 作业1已布置。请于3月8日中午12点前提交。
- 2月10日: 选课的同学请参与此关于编程基础的问卷调查。
  - 学硕同学请点击这里：[《量化投资》课前调查](https://www.wjx.cn/vm/YVvoldj.aspx#) 。
  - 专硕同学请点击这里：[《金融数据分析》课前调查](https://www.wjx.cn/vm/QEMysHB.aspx#)。


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

This course does not contain high-frequency (intraday) strategies, or strategies involving derivatives . Please refer to other courses provided by the school if these are what you need. Our main data is from A shares of China's stock markets.

<!-- Some of the above mentioned fields are fast developing (e.g. machine learning applications), and thus the contents may be subject to change. -->

## 1.1 知识储备 Prerequisites
应当知道基本的计量经济学(如必要我们会进行简短的复习)。无需具备编程知识，所有的编程相关的内容都会在课程中介绍，但如果有编程经验更好。面对大量的编程应当有心理准备。

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
- Geron, Aurelien, 2019, *Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow*. 2nd Edition (O'Reilly).

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

<style type="text/css">
.tg  {border-collapse:collapse;border-color:#ccc;border-spacing:0;}
.tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-v16d{background-color:#f9f9f9;border-color:#cccccc;text-align:left;vertical-align:top}
.tg .tg-65iu{border-color:#cccccc;text-align:left;vertical-align:top}
.tg .tg-o57c{border-color:#cccccc;text-align:center;vertical-align:top}
</style>
<table class="tg">
<colgroup>
<col style="width: 56px">
<col style="width: 114px">
<col style="width: 298px">
<col style="width: 108px">
<col style="width: 142px">
<col style="width: 78px">
</colgroup>
<thead>
  <tr>
    <th class="tg-o57c">Lecture</th>
    <th class="tg-o57c">Date</th>
    <th class="tg-o57c">Topics</th>
    <th class="tg-o57c">Materials</th>
    <th class="tg-o57c">Readings</th>
    <th class="tg-o57c">Homework</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-v16d">1</td>
    <td class="tg-v16d">Feb 13, 14</td>
    <td class="tg-v16d">1. General introduction <br>2. Introduction to Python</td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2023/lec1/Intro.pdf" target="_blank" rel="noopener noreferrer">Intro.pdf</a> <br>
    <a href="/assets/courses/quant_2023/lec1/Python_intro.ipynb" target="_blank" rel="noopener noreferrer">Python_intro.ipynb</a> <br>
    <a href="/assets/courses/quant_2023/lec1/Python_intro.html" target="_blank" rel="noopener noreferrer">Python_intro.html</a> <br>
    <a href="/assets/courses/quant_2023/lec1/others.zip" target="_blank" rel="noopener noreferrer">others.zip</a> <br>
    <a href="https://www.aliyundrive.com/s/Zkgjv7Wj4HR" target="_blank" rel="noopener noreferrer">[Video-Lec1]</a>
    </td>
    <td class="tg-v16d">
    <a href="https://www.liaoxuefeng.com/wiki/1016959663602400" target="_blank" rel="noopener noreferrer">廖雪峰的Python教程</a>
    </td>
    <td class="tg-v16d"></td>
  </tr>
  <tr>
    <td class="tg-65iu">2</td>
    <td class="tg-65iu">Feb 20, 21</td>
    <td class="tg-65iu">1. Introduction to data science packages<br>2. Introduction to backtesting platforms (Uqer)</td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2023/lec2/np_pd_plot.ipynb" target="_blank" rel="noopener noreferrer">np_pd_plot.ipynb</a> <br>
    <a href="/assets/courses/quant_2023/lec2/np_pd_plot.html" target="_blank" rel="noopener noreferrer">np_pd_plot.html</a> <br>
    <a href="/assets/courses/quant_2023/lec2/strategy_example_202302.ipynb" target="_blank" rel="noopener noreferrer">strategy_example_202302.ipynb</a> <br>
    <a href="/assets/courses/quant_2023/lec2/strategy_example_202302.pdf" target="_blank" rel="noopener noreferrer">strategy_example_202302.pdf</a>
    <a href="https://uqer.datayes.com/pro/pro_download.html" target="_blank" rel="noopener noreferrer">优矿客户端下载地址</a> <br>
    <a href="https://www.aliyundrive.com/s/s2at4BBNwSn" target="_blank" rel="noopener noreferrer">[Video-Lec2]</a>
    </td>
    <td class="tg-65iu">
    <a href="https://pandas.pydata.org/docs/user_guide/index.html" target="_blank" rel="noopener noreferrer">pandas' user guide</a> <br>
    优矿相关文档
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2023/exercises/ex1.zip" target="_blank" rel="noopener noreferrer">ex1.zip</a> (due: Mar.08 noon)
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">3</td>
    <td class="tg-v16d">Feb 27, 28</td>
    <td class="tg-v16d">1. Exploratory data analysis<br>2. Introduction to factor models and related econometrics</td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2023/lec3/Newey-West.pdf" target="_blank" rel="noopener noreferrer">Newey-West.pdf</a> <br>
    <a href="/assets/courses/quant_2023/lec3/econometrics_summary.pdf" target="_blank" rel="noopener noreferrer">econometrics_summary.pdf</a> <br>
    <a href="/assets/courses/quant_2023/lec3/1-EDA.ipynb" target="_blank" rel="noopener noreferrer">1-EDA.ipynb</a> <br>
    <a href="/assets/courses/quant_2023/lec3/1-EDA.html" target="_blank" rel="noopener noreferrer">1-EDA.html</a> <br>
    <a href="https://www.aliyundrive.com/s/vn1r5Ji78k8" target="_blank" rel="noopener noreferrer">[Video-lec3]</a>
    </td>
    <td class="tg-v16d">
    Cochrane (2005), Ch. 12 <br>
    <a href="https://www.jstor.org/stable/1913610?searchText=&searchUri=&ab_segments=&searchKey=&refreqid=fastly-default%3A0a291a66dc09884f01c5730c91489cfe" target="_blank" rel="noopener noreferrer">Newey & West (1987)</a> <br>
    石川, 刘洋溢, & 连祥斌. (2020). 因子投资：方法与实践, Ch. 2
    </td>
    <td class="tg-v16d"></td>
  </tr>
  <tr>
    <td class="tg-65iu">4</td>
    <td class="tg-65iu">Mar 6, 7</td>
    <td class="tg-65iu">Fama-French 3 factors</td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2023/lec4/2-sort_FMreg_on_beta_size.ipynb" target="_blank" rel="noopener noreferrer">2-sort_FMreg_on_beta_size.ipynb</a> <br>
    <a href="/assets/courses/quant_2023/lec4/2-sort_FMreg_on_beta_size.html" target="_blank" rel="noopener noreferrer">2-sort_FMreg_on_beta_size.html</a> <br>
    <a href="/assets/courses/quant_2023/lec4/3-FF3.ipynb" target="_blank" rel="noopener noreferrer">3-FF3.ipynb</a> <br>
    <a href="/assets/courses/quant_2023/lec4/3-FF3.html" target="_blank" rel="noopener noreferrer">3-FF3.html</a> <br>
    <a href="https://www.aliyundrive.com/s/UMeDvT9iwzD" target="_blank" rel="noopener noreferrer">[Video-lec4]</a> <br>
    </td>
    <td class="tg-65iu">
    <a href="https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.1992.tb04398.x" target="_blank" rel="noopener noreferrer">Fama & French (1992)</a> <br>
    <a href="https://www.sciencedirect.com/science/article/abs/pii/0304405X93900235" target="_blank" rel="noopener noreferrer">Fama & French (1993)</a> <br>
    <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3038446" target="_blank" rel="noopener noreferrer">Lee et al. (2017)</a> <br>
    <a href="https://www.sciencedirect.com/science/article/pii/S0304405X19300625" target="_blank" rel="noopener noreferrer">Liu et al. (2019)</a>
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2023/exercises/ex2.pdf" target="_blank" rel="noopener noreferrer">ex2.pdf</a> (due: Mar.22 noon)
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">5</td>
    <td class="tg-v16d">Mar 13, 14</td>
    <td class="tg-v16d">1. Other common factors: Momentum, Reversal, Liquidity, Volatility <br>
    2. Applications of factor models
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2023/lec5/other_factors.zip" target="_blank" rel="noopener noreferrer">other_factors.zip</a> <br>
    <a href="/assets/courses/quant_2023/lec5/backtest.zip" target="_blank" rel="noopener noreferrer">backtest.zip</a> <br>
    <a href="/assets/courses/quant_2023/lec5/factor_application.zip" target="_blank" rel="noopener noreferrer">factor_application.zip</a> <br>
    <a href="/assets/courses/quant_2023/lec5/factor_func.py" target="_blank" rel="noopener noreferrer">factor_func.py</a> <br>
    <a href="/assets/courses/quant_2023/lec5/bootstrap.zip" target="_blank" rel="noopener noreferrer">bootstrap.zip</a> <br>
    <a href="https://www.aliyundrive.com/s/RyVXkEjYUmX" target="_blank" rel="noopener noreferrer">[Video-lec5]</a> <br>
    </td>
    <td class="tg-v16d">
    See refs in lecture notes
    </td>
    <td class="tg-v16d"></td>
  </tr>
  <tr>
    <td class="tg-65iu">6</td>
    <td class="tg-65iu">Mar 20, 21</td>
    <td class="tg-65iu">1. Introduction to technical analysis and related econometrics <br>
    2. Statistical tests of technical analysis indicators
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2023/lec6/技术分析的基本思想和统计检验.pdf" target="_blank" rel="noopener noreferrer">技术分析的基本思想和统计检验.pdf</a> <br>
    <a href="/assets/courses/quant_2023/lec6/7-ta_test.html" target="_blank" rel="noopener noreferrer">7-ta_test.html</a> <br>
    <a href="/assets/courses/quant_2023/lec6/7-ta_test.ipynb" target="_blank" rel="noopener noreferrer">7-ta_test.ipynb</a> <br>
    <a href="https://www.aliyundrive.com/s/cztsFzfr9rK" target="_blank" rel="noopener noreferrer">[Video-lec6]</a>
    </td>
    <td class="tg-65iu">
    See refs in lecture notes
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2023/exercises/ex3.pdf" target="_blank" rel="noopener noreferrer">ex3.pdf</a> (due: Apr.05 noon)
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">7</td>
    <td class="tg-v16d">Mar 27, 28</td>
    <td class="tg-v16d">Introduction to Machine Learning methods</td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2023/lec7/7-crs_and_timing.ipynb" target="_blank" rel="noopener noreferrer">7-crs_and_timing.ipynb</a> <br>
    <a href="/assets/courses/quant_2023/lec7/ML.pdf" target="_blank" rel="noopener noreferrer">ML.pdf </a> <br>
    <a href="/assets/courses/quant_2023/lec7/entropy.pdf" target="_blank" rel="noopener noreferrer">entropy.pdf</a> <br>
    <a href="https://www.aliyundrive.com/s/ru5BnvttoKh" target="_blank" rel="noopener noreferrer">[Video-lec7]</a>
    </td>
    <td class="tg-v16d">
    <a href="https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646" target="_blank" rel="noopener noreferrer">Géron (2019)</a>
    </td>
    <td class="tg-v16d"></td>
  </tr>
  <tr>
    <td class="tg-65iu">8</td>
    <td class="tg-65iu">Apr 3, 4</td>
    <td class="tg-65iu">Applications of Machine Learning to factor models and technical analysis</td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2023/lec8/Wu et al.pdf" target="_blank" rel="noopener noreferrer">Wu et al.pdf </a> <br>
    <a href="/assets/courses/quant_2023/lec8/pca.pdf" target="_blank" rel="noopener noreferrer">pca.pdf </a> <br>
    <a href="/assets/courses/quant_2023/lec8/8-factor_ML.ipynb" target="_blank" rel="noopener noreferrer">8-factor_ML.ipynb </a> <br>
    <a href="/assets/courses/quant_2023/lec8/8-factor_ML.html" target="_blank" rel="noopener noreferrer">8-factor_ML.html </a> <br>
    <a href="/assets/courses/quant_2023/lec8/8-ta_ML.ipynb" target="_blank" rel="noopener noreferrer">8-ta_ML.ipynb (4月6日更新, RSI指标计算有错。感谢庄源同学。) </a> <br>
    <a href="/assets/courses/quant_2023/lec8/8-ta_ML.html" target="_blank" rel="noopener noreferrer">8-ta_ML.html (4月6日更新, RSI指标计算有错。感谢庄源同学。)  </a> <br>
    <a href="https://www.aliyundrive.com/s/TwtABgJVzcg" target="_blank" rel="noopener noreferrer">[Video-lec8]</a>
    </td>
    <td class="tg-65iu">
    <a href="https://academic.oup.com/rfs/article/33/5/2223/5758276?login=false" target="_blank" rel="noopener noreferrer">Gu et al. (2020) </a> <br>
    <a href="https://www.sciencedirect.com/science/article/pii/S0304405X21003743" target="_blank" rel="noopener noreferrer">Leippold (2021) </a>
    </td>
    <td class="tg-65iu"></td>
  </tr>
  <tr>
    <td class="tg-v16d">Exam</td>
    <td class="tg-v16d">考题将于4月12日布置</td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2023/exam.pdf" target="_blank" rel="noopener noreferrer">exam.pdf </a> <br>
    <a href="https://share.weiyun.com/L6hnDxYt" target="_blank" rel="noopener noreferrer">data.zip</a>
    </td>
    <td class="tg-v16d"></td>
    <td class="tg-v16d"></td>
    <td class="tg-v16d"></td>
  </tr>
</tbody>
</table>

<!-- # 2. 课件 Materials
## Lecture 1. Introduction to Python

[lec-1.pdf](/assets/courses/quant/lec1/lec-1.pdf)

[Python_intro.ipynb](/assets/courses/quant/lec1/Python_intro.ipynb)

[Python_intro.html](/assets/courses/quant/lec1/Python_intro.html)

[[Lecture video]](https://www.aliyundrive.com/s/hkzXpqb6HAC)

## Lecture 2. Introduction to Data Science Packages and Uqer Platform

numpy, pandas, plottting introduction: [np_pd_plot.ipynb](/assets/courses/quant/lec2/np_pd_plot.ipynb), [np_pd_plot.html](/assets/courses/quant/lec2/np_pd_plot.html)

Uqer strategy example: [strategy_example_202202.ipynb](/assets/courses/quant/lec2/strategy_example_202202.ipynb)，[strategy_example_202202.html](/assets/courses/quant/lec2/strategy_example_202202.html)，[优矿量化投资策略教程示例文件](/assets/courses/quant/lec2/量化投资策略教程示例文件.nb)

[[Uqer intro video]](https://www.aliyundrive.com/s/y48DZ4kc7Vm)

[[Lecture video]](https://www.aliyundrive.com/s/Ldg4eiYUoAi)

## Lecture 3. Exploratory Data Analysis & Introduction to Factor Models

Quick review of robust errors: [crash_note.pdf](/assets/courses/quant/lec3/crash_note.pdf)

Fundamental econometrics related to factor models: [econometrics_summary.ipynb](/assets/courses/quant/lec3/econometrics_summary.ipynb), [econometrics_summary.pdf](/assets/courses/quant/lec3/econometrics_summary.pdf)

Exploratory Data Analysis: [1-EDA.ipynb](/assets/courses/quant/lec3/1-EDA.ipynb), [1-EDA.html](/assets/courses/quant/lec3/1-EDA.html)

[[Lecture video]](https://www.aliyundrive.com/s/xEBcpr2H48w)

## Lecture 4. Sorting, Fama-MacBeth Regression, Fama French 3 Factors

(Updated on 2022.03.15) Sorting and FM regression on beta, size: [2-sort_FMreg_on_beta_size.ipynb](/assets/courses/quant/lec4/2-sort_FMreg_on_beta_size.ipynb), [2-sort_FMreg_on_beta_size.html](/assets/courses/quant/lec4/2-sort_FMreg_on_beta_size.html)

(Updated on 2022.03.15) Fama-French 3 factors: [3-FF3.ipynb](/assets/courses/quant/lec4/3-FF3.ipynb), [3-FF3.html](/assets/courses/quant/lec4/3-FF3.html)

[[Lecture video]](https://www.aliyundrive.com/s/1U7Z57PRU1Q)

## Lecture 5. Momentum, Reversal, Liquidity, Volatility Factors.

Momentum and reversal: [4-momentum_reversal.ipynb](/assets/courses/quant/lec5/4-momentum_reversal.ipynb), [4-momentum_reversal.html](/assets/courses/quant/lec5/4-momentum_reversal.html)

Wrapping code for creating factors: [factors.ipynb](/assets/courses/quant/lec5/factors.ipynb), [factors.html](/assets/courses/quant/lec5/factors.html)

(Updated on 2022.03.22) Liquidity and volatility: [5-liquidity_volatility.ipynb](/assets/courses/quant/lec5/5-liquidity_volatility.ipynb), [5-liquidity_volatility.html](/assets/courses/quant/lec5/5-liquidity_volatility.html)

Code used in "myutils": [code_in_myutils.zip](/assets/courses/quant/lec5/code_in_myutils.zip)

[[Lecture video]](https://www.aliyundrive.com/s/BVH69sitQoD)

## Lecture 6. Applications of Factor Models. Introduction to Technical Analysis and Related Econometrics

(updated 2022.03.23) Applications of factor models: [6-factor_application.ipynb](/assets/courses/quant/lec6/6-factor_application.ipynb), [6-factor_application.html](/assets/courses/quant/lec6/6-factor_application.html)

(updated 2022.03.23) Backtesting with uqer, cross sectional selection of stocks: [6-backtest.ipynb](/assets/courses/quant/lec6/6-backtest.ipynb)

(updated 2022.03.29)Ideas of Technical Analysis: [技术分析的基本思想和统计检验.pdf](/assets/courses/quant/lec6/技术分析的基本思想和统计检验.pdf)

[[Lecture video]](https://www.aliyundrive.com/s/hmXca91rFMF)

## Lecture 7. Statistical Tests of Technical Indicators. Introduction to Machine Learning Methods

Bootstrap review: [bootstrap.R](/assets/courses/quant/lec7/bootstrap.R), [bootstrapping.pdf](/assets/courses/quant/lec7/bootstrapping.pdf)

(updated 2022.03.29)Statistical tests of technical indicators: [7-ta_test.ipynb](/assets/courses/quant/lec7/7-ta_test.ipynb), [7-ta_test.html](/assets/courses/quant/lec7/7-ta_test.html)

Backtests with both stock-picking and market timing: [7-crs_and_timing.ipynb](/assets/courses/quant/lec7/7-crs_and_timing.ipynb)


[[Lecture video]](https://www.aliyundrive.com/s/ieGosujLZe5)

## Lecture 8. Applications of Machine Learning to Factor Models and Technical Analysis

[Gu et al. (2020)](/assets/courses/quant/lec8/Gu-2020.pdf)

[Wu et al. (2019)](/assets/courses/quant/lec8/Wu-2019.pdf)

[Leippold et al. (2021)](/assets/courses/quant/lec8/Leippold-2021.pdf)

Machine learning applications in factor models: [8-factor_ML.ipynb](/assets/courses/quant/lec8/8-factor_ML.ipynb), [8-factor_ML.html](/assets/courses/quant/lec8/8-factor_ML.html)

Machine learning applications in technical analysis: [8-ta_ML.ipynb](/assets/courses/quant/lec8/8-ta_ML.ipynb), [8-ta_ML.html](/assets/courses/quant/lec8/8-ta_ML.html)

[[Lecture video]](https://www.aliyundrive.com/s/r273NKAGJwg)

# 致谢

这门课是南开大学“智能投顾虚拟教研室”的线上公开课之一。感谢南开大学金融学院领导、刘澜飚教授和周爱民教授的大力支持！感谢[优矿](https://uqer.datayes.com/)、[同花顺](https://www.10jqka.com.cn/)、[悟空投资](https://www.wukongtz.com/)对虚拟教研室以及本课程的大力支持！ -->

-----
[Back to top](#)