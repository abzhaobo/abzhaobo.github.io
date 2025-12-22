---
layout: page
title: 量化投资/金融数据分析 Quantitative Investment (2024)
description: Factor models, empirical tests of technical analysis indicators, applications of machine learning techniques
img: assets/img/quant2024.png
importance: 2
category: Earlier
---

- [❗️通知 Announcement❗️](#️通知-announcement️)
- [1. 课程大纲 Syllabus](#1-课程大纲-syllabus)
  - [1.1 知识储备 Prerequisites](#11-知识储备-prerequisites)
  - [1.2 课本和参考书 Textbook and References](#12-课本和参考书-textbook-and-references)
  - [1.3 评分方式 Grading](#13-评分方式-grading)
- [2. 课程内容 Contents](#2-课程内容-contents)

# ❗️通知 Announcement❗️
- 2024 课程评价

    [课程评价统计报告](/assets/courses/quant_2024/report2024.pdf)
- 6月3日: 讲座：《中国可转债市场与投资实践》。时间：2024年6月11日20:00。主讲嘉宾：吴江宏，汇添富基金管理股份有限公司稳健收益部总经理。飞书会议： https://vc.feishu.cn/j/375316373
- 4月22日: 作业3已布置。请于5月13日前提交。
- 4月1日: 作业2已布置。请于4月22日前提交。
- 3月11日: 作业1已布置。请于3月25日前提交。

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
- 3到4次作业 (60%)
- 家庭考试 (40%)。大致形式为在规定时间内完成策略构建。

- 3 or 4 homework exercises (60%)
- take-home exam (40%)

**抄袭作业零容忍。抄袭他人作业可能会直接挂科。** 对于编程经验较少的同学来说，遇到困难是正常的。所有的代码我都会共享，只要仔细研读一定可以完成作业和考试。请相信自己。

**PLAGIARISM IS STRICTLY PROHIBITED. You may immediately fail the course if copy-pasting other's work.** It will be normal to meet obstacles during the course, especially for students with less exposure to programming. I'll share all relevant codes and you'll surely complete the course successfully if you read and try the provided codes with some care. Please trust yourself and hang on.

</details>

&nbsp;

# 2. 课程内容 Contents

课程录屏在飞书群

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
    <td class="tg-v16d">3月4日</td>
    <td class="tg-v16d">1. General introduction <br>2. Introduction to Python</td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2024/lec1/lec1.zip" target="_blank" rel="noopener noreferrer">lec1.zip</a> <br>
    <a href="/assets/courses/quant_2023/lec1/Python_intro.html" target="_blank" rel="noopener noreferrer">Python_intro.html</a>
    </td>
    <td class="tg-v16d">
    <a href="https://www.liaoxuefeng.com/wiki/1016959663602400" target="_blank" rel="noopener noreferrer">廖雪峰的Python教程</a>
    </td>
    <td class="tg-v16d"></td>
  </tr>
  <tr>
    <td class="tg-65iu">2</td>
    <td class="tg-65iu">3月11日</td>
    <td class="tg-65iu">1. Introduction to Python <br>2. Introduction to Numpy, Pandas, Matplotlib </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2024/lec2/np_pd_plot.ipynb" target="_blank" rel="noopener noreferrer">np_pd_plot.ipynb</a> <br>
    <a href="/assets/courses/quant_2024/lec2/np_pd_plot.html" target="_blank" rel="noopener noreferrer">np_pd_plot.html</a> <br>
     <a href="https://nankai.feishu.cn/file/FAzXbMtEDo8zv6xpWCzcpdGmnlh" target="_blank" rel="noopener noreferrer">stk_df_2015_2021.zip</a> <br>
    </td>
    <td class="tg-65iu">
    <a href="https://pandas.pydata.org/docs/user_guide/index.html" target="_blank" rel="noopener noreferrer">pandas' user guide</a> <br>
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2024/exercises/ex1.zip" target="_blank" rel="noopener noreferrer">ex1.zip</a> (截止日期: 3月25日)
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">3</td>
    <td class="tg-v16d">3月18日</td>
    <td class="tg-v16d">1. Introduction to Uqer (优矿) <br> 2. Exploratory data analysis </td>
    <td class="tg-v16d">
     <a href="/assets/courses/quant_2024/lec3/strategy_example_202403.pdf" target="_blank" rel="noopener noreferrer">strategy_example_202403.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec3/1-EDA.html" target="_blank" rel="noopener noreferrer">1-EDA.html</a> <br>
    <a href="/assets/courses/quant_2024/lec3/1-EDA.ipynb" target="_blank" rel="noopener noreferrer">1-EDA.ipynb</a> <br>
    <a href="https://nankai.feishu.cn/file/WDImbTQ0BoWQ7ExVZVVcTlqWnF1" target="_blank" rel="noopener noreferrer">stk_df_2016_2024.zip</a> <br>
    </td>
    <td class="tg-v16d">
    <a href="https://uqer.datayes.com/pro/pro_download.html" target="_blank" rel="noopener noreferrer">优矿客户端下载地址</a> <br>
    优矿帮助文档
    </td>
    <td class="tg-v16d"></td>
  </tr>
  <tr>
    <td class="tg-65iu">4</td>
    <td class="tg-65iu">3月25日</td>
    <td class="tg-65iu"> Introduction to factor models and related econometrics </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2024/lec4/Newey_West.pdf" target="_blank" rel="noopener noreferrer">Newey_West.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec4/econometrics_summary.pdf" target="_blank" rel="noopener noreferrer">econometrics_summary.pdf</a>
    </td>
    <td class="tg-65iu">
    <a href="https://www.jstor.org/stable/1913610?searchText=&searchUri=&ab_segments=&searchKey=&refreqid=fastly-default%3A0a291a66dc09884f01c5730c91489cfe" target="_blank" rel="noopener noreferrer">Newey & West (1987)</a> <br>
    Cochrane (2005), Ch. 12 <br>
    石川, 刘洋溢, & 连祥斌. (2020). 因子投资：方法与实践, Ch. 2
    </td>
    <td class="tg-65iu">
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">5</td>
    <td class="tg-v16d">4月1日</td>
    <td class="tg-v16d">
    1. Econometrics continued <br>
    2. Sorting on Beta and Size
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2024/lec5/2-sort_FMreg_on_beta_size.html" target="_blank" rel="noopener noreferrer">2-sort_FMreg_on_beta_size.html</a> <br>
    <a href="/assets/courses/quant_2024/lec5/2-sort_FMreg_on_beta_size.ipynb" target="_blank" rel="noopener noreferrer">2-sort_FMreg_on_beta_size.ipynb</a> <br>
    <a href="https://nankai.feishu.cn/file/B9E9b1Dcoo6nzPxWIRqcn9LVn9d" target="_blank" rel="noopener noreferrer">beta_rf_stk.zip</a>
    </td>
    <td class="tg-v16d">
    <a href="https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.1992.tb04398.x" target="_blank" rel="noopener noreferrer">Fama & French (1992)</a> <br>
    <a href="https://www.sciencedirect.com/science/article/abs/pii/0304405X93900235" target="_blank" rel="noopener noreferrer">Fama & French (1993)</a> <br>
    石川, 刘洋溢, & 连祥斌. (2020). 因子投资：方法与实践, Ch. 2, Ch. 3
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2024/exercises/ex2.pdf" target="_blank" rel="noopener noreferrer">ex2.pdf</a> (截止日期: 4月22日)
    </td>
  </tr>
  <tr>
    <td class="tg-65iu">6</td>
    <td class="tg-65iu">4月8日</td>
    <td class="tg-65iu">
    1. Fama-French 3 factors <br>
    2. Other common factors: Momentum, Reversal, Liquidity, Volatility
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2024/lec6/3-FF3.html" target="_blank" rel="noopener noreferrer">3-FF3.html</a> <br>
    <a href="/assets/courses/quant_2024/lec6/3-FF3.ipynb" target="_blank" rel="noopener noreferrer">3-FF3.ipynb</a> <br>
    <a href="https://nankai.feishu.cn/file/V9gcbDNa4oHhFNxvgn6cAJ44neh" target="_blank" rel="noopener noreferrer">data_0408.zip</a>
    </td>
    <td class="tg-65iu">
    <a href="https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.1992.tb04398.x" target="_blank" rel="noopener noreferrer">Fama & French (1992)</a> <br>
    <a href="https://www.sciencedirect.com/science/article/abs/pii/0304405X93900235" target="_blank" rel="noopener noreferrer">Fama & French (1993)</a> <br>
    石川, 刘洋溢, & 连祥斌. (2020). 因子投资：方法与实践, Ch. 2, Ch. 3
    </td>
    <td class="tg-65iu">
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">7</td>
    <td class="tg-v16d">4月15日</td>
    <td class="tg-v16d">
    1. Momentum, reversal, liquidity, volatility factors <br>
    2. Applications of factor models
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2024/lec7/4-momentum_reversal.html" target="_blank" rel="noopener noreferrer">4-momentum_reversal.html</a> <br>
    <a href="/assets/courses/quant_2024/lec7/5-daily_factors.html" target="_blank" rel="noopener noreferrer">5-daily_factors.html</a> <br>
    <a href="/assets/courses/quant_2024/lec7/5-liquidity_volatility.html" target="_blank" rel="noopener noreferrer">5-liquidity_volatility.html</a> <br>
    <a href="/assets/courses/quant_2024/lec7/6-factor_application.html" target="_blank" rel="noopener noreferrer">6-factor_application.html</a> <br>
    <a href="/assets/courses/quant_2024/lec7/6-backtest.pdf" target="_blank" rel="noopener noreferrer">6-backtest.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec7/ipynb_files.zip" target="_blank" rel="noopener noreferrer">ipynb_files.zip</a>
    </td>
    <td class="tg-v16d">
    参考文献见课件中所列
    </td>
    <td class="tg-v16d">
    </td>
  </tr>
  <tr>
    <td class="tg-65iu">8</td>
    <td class="tg-65iu">4月22日</td>
    <td class="tg-65iu">
    1. Introduction to technical analysis and related econometrics <br>
    2. Statistical tests of technical analysis indicators
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2024/lec8/bootstrapping.pdf" target="_blank" rel="noopener noreferrer">bootstrapping.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec8/bootstrap_code.zip" target="_blank" rel="noopener noreferrer">bootstrap_code.zip</a> <br>
    <a href="/assets/courses/quant_2024/lec8/技术分析的基本思想和统计检验.pdf" target="_blank" rel="noopener noreferrer">技术分析的基本思想和统计检验.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec8/7-ta_test.html" target="_blank" rel="noopener noreferrer">7-ta_test.html</a> <br>
    <a href="/assets/courses/quant_2024/lec8/7-ta_test.ipynb" target="_blank" rel="noopener noreferrer">7-ta_test.ipynb</a> <br>
    <a href="https://nankai.feishu.cn/file/Q7QrbKHfNo0AsrxUDeec6KCrnQe" target="_blank" rel="noopener noreferrer">stk_ta_df.zip</a>
    </td>
    <td class="tg-65iu">
    参考文献见课件中所列
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2024/exercises/ex3.pdf" target="_blank" rel="noopener noreferrer">ex3.pdf</a> (截止日期: 5月13日)
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">9</td>
    <td class="tg-v16d">4月29日</td>
    <td class="tg-v16d">
    1. The data snooping problem <br>
    2. Introduction to Machine Learning methods </td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2024/lec9/7-crs_and_timing.pdf" target="_blank" rel="noopener noreferrer">7-crs_and_timing.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec9/7-crs_and_timing.ipynb" target="_blank" rel="noopener noreferrer">7-crs_and_timing.ipynb</a> <br>
    <a href="/assets/courses/quant_2024/lec9/ML.pdf" target="_blank" rel="noopener noreferrer">ML.pdf</a> <br>
    </td>
    <td class="tg-v16d">
    参考文献见课件中所列
    </td>
    <td class="tg-v16d"> </td>
  </tr>
  <tr>
    <td class="tg-v16d">10</td>
    <td class="tg-v16d">5月6日</td>
    <td class="tg-v16d">
    1. Introduction to Machine Learning methods <br>
    2. Applications of Machine Learning
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2024/lec10/ML.pdf" target="_blank" rel="noopener noreferrer">ML.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec10/ridge vs. lasso.pdf" target="_blank" rel="noopener noreferrer">ridge vs. lasso.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec10/entropy.pdf" target="_blank" rel="noopener noreferrer">entropy.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec10/8-ta_ML.ipynb" target="_blank" rel="noopener noreferrer">8-ta_ML.ipynb</a> <br>
    <a href="/assets/courses/quant_2024/lec10/8-ta_ML.html" target="_blank" rel="noopener noreferrer">8-ta_ML.html</a>
    </td>
    <td class="tg-v16d">
    <a href="https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow-ebook/dp/B0BHCFNY9Q?ref_=ast_author_dp&dib=eyJ2IjoiMSJ9.HYk1fun9wcouHZdScULxJ5ZpV2FWtcUU2Nn8Gnh6ttoCQUnLJGJRfvoNVfq91dydUjgYHOrsctvc1sSG1iqUkZ0Qu9NkuqDYu-6_kKjn569c83lMzJBJ6axHHyqAzuf3_HoDS18FmBDBI6J336XOvDLlh1NDdZ_NFGC-K29YAn3OSuoy-uVTbJidkTkocifXTbhn2TMJ5m9Vpf9iDmcXQ6aJcTtxh5Ga8nmyee0zTYw.x7bQT7M7dVJaKd5o8bw0rL_Ib8dMiogFTAZJ9aaUh9k&dib_tag=AUTHOR" target="_blank" rel="noopener noreferrer">Geron (2022)</a>
    </td>
    <td class="tg-v16d"> </td>
  </tr>
  <tr>
    <td class="tg-v16d">11</td>
    <td class="tg-v16d">5月13日</td>
    <td class="tg-v16d">
    Applications of Machine Learning
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2024/lec11/吴 et al-机器学习视角下中国股票资产收益率可预测性研究.pdf" target="_blank" rel="noopener noreferrer">吴 et al-机器学习视角下中国股票资产收益率可预测性研究.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec11/Principal Component Analysis.pdf" target="_blank" rel="noopener noreferrer">Principal Component Analysis.pdf</a> <br>
    <a href="/assets/courses/quant_2024/lec11/8-factor_ML.ipynb" target="_blank" rel="noopener noreferrer">8-factor_ML.ipynb</a> <br>
    <a href="/assets/courses/quant_2024/lec11/8-factor_ML.html" target="_blank" rel="noopener noreferrer">8-factor_ML.html</a>
    </td>
    <td class="tg-v16d">
    <a href="https://academic.oup.com/rfs/article/33/5/2223/5758276?login=false" target="_blank" rel="noopener noreferrer">Gu et al. (2020) </a> <br>
    <a href="https://www.sciencedirect.com/science/article/pii/S0304405X21003743" target="_blank" rel="noopener noreferrer">Leippold (2021) </a>
    </td>
    <td class="tg-v16d"> </td>
  </tr>
</tbody>
</table>

-----
[Back to top](#)