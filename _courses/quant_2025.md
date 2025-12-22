---
layout: page
title: 量化投资/金融数据分析 Quantitative Investment (2025)
description: Factor models, empirical tests of technical analysis indicators, applications of machine learning techniques
img: assets/img/quant2025.png
importance: 1
category: Earlier
giscus_comments: true
---

- [❗️通知 Announcement❗️](#️通知-announcement️)
- [1. 课程大纲 Syllabus](#1-课程大纲-syllabus)
  - [1.1 知识储备 Prerequisites](#11-知识储备-prerequisites)
  - [1.2 课本和参考书 Textbook and References](#12-课本和参考书-textbook-and-references)
  - [1.3 评分方式 Grading](#13-评分方式-grading)
- [2. 课程内容 Contents](#2-课程内容-contents)

# ❗️通知 Announcement❗️
- 🎉🎉讲座：《逆向思维在投资和就业上的应用》。嘉宾：翟效华，曾任东方财富证券副总经理，资产管理部总监。**时间：5月29日下午3点**。地点：金融学院203。[回放](https://nankai.feishu.cn/minutes/obcnra7s5uf754fg3i9ypl4i?from=from_copylink)
- **2025.05.07: [期末考题](/assets/courses/quant_2025/exam.pdf)已布置，请于2025年6月30日前提交至 zhaobo@nankai.edu.cn 。**
- **2025.04.09: 第二次[作业](/assets/courses/quant_2025/exercises/ex2.pdf)已布置，请于2025年4月23日前提交至 zhaobo@nankai.edu.cn 。**
- **2025.03.05: 第一次[作业](/assets/courses/quant_2025/exercises/ex1.pdf)已布置，请于2025年3月19日前提交至 zhaobo@nankai.edu.cn 。**
- 请分组，组长需提供姓名、手机号、邮箱，以便开通优矿平台账号
- 课前问卷调察：[https://www.wjx.cn/vm/YlnrbHM.aspx](https://www.wjx.cn/vm/YlnrbHM.aspx)


# 1. 课程大纲 Syllabus

<!-- &nbsp; -->

<details markdown="1">
  <summary> 详细内容 Details </summary>

这门课程在教学计划上有两个不同的名称：《量化投资》(学硕)，《金融数据分析和Python应用》(专硕)。主要讨论用数量方法探索金融数据以及构建交易策略。课程内容是应用导向的，但相关的理论也会有涉及。课程目标：掌握基本的工具以及用数据分析的思维方式。这门课主要包含以下内容：
- Python 基础以及数据处理相关库(numpy, pandas, sklearn, tensorflow, keras等)
- 因子模型
- 技术分析介绍以及统计检验
- 机器学习和深度学习在量化投资中的应用

这门课暂不包含高频数据(日内)策略，也不包含衍生品策略。主要的数据来源是中国A股市场股票数据

This is a course about constructing trading strategies by quantitative methods. The course is application oriented, but relevant theories will also be discussed. The course objective is to teach students basic tools and ways of exploring financial data so that quantitative (and perhaps winning) strategies can be constructed. The main contents are:
- introduction of Python basics and data science packages (numpy, pandas, sklearn, tensorflow, keras, etc.)
- construction of factor models
- introduction to technical analysis
- application of machine learning and deep learning methods

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
- 3次作业 (75%)
- 开放式项目 (25%)

- 3 homework exercises (75%)
- An open-ended project (25%)

**抄袭作业零容忍。抄袭他人作业可能会直接挂科。** 对于编程经验较少的同学来说，遇到困难是正常的。所有的代码我都会共享，只要仔细研读一定可以完成作业和考试。请相信自己。

**PLAGIARISM IS STRICTLY PROHIBITED. You may immediately fail the course if copy-pasting other's work.** It will be normal to meet obstacles during the course, especially for students with less exposure to programming. I'll share all relevant codes and you'll surely complete the course successfully if you read and try the provided codes with some care. Please trust yourself and hang on.

</details>

&nbsp;

# 2. 课程内容 Contents

<style type="text/css">
.tg  { 
    border-collapse:collapse;
    border-color:#ccc;
    border-spacing:0;
    width: 100%; /* Increase the width of the whole table */
    table-layout: auto; /* Adjusts based on content */
}
.tg td {
    background-color:#fff;
    border-color:#ccc;
    border-style:solid;
    border-width:1px;
    color:#333;
    font-family:Arial, sans-serif;
    font-size:16px;
    overflow:hidden;
    padding:10px 5px;
    word-break:normal;
}
.tg th {
    background-color:#f0f0f0;
    border-color:#ccc;
    border-style:solid;
    border-width:1px;
    color:#333;
    font-family:Arial, sans-serif;
    font-size:16px;
    font-weight:normal;
    overflow:hidden;
    padding:10px 5px;
    word-break:normal;
}
.tg .tg-v16d {
    background-color:#f9f9f9;
    border-color:#cccccc;
    text-align:left;
    vertical-align:top;
}
.tg .tg-65iu {
    border-color:#cccccc;
    text-align:left;
    vertical-align:top;
}
.tg .tg-o57c {
    border-color:#cccccc;
    text-align:center;
    vertical-align:top;
}
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
    <td class="tg-v16d">2月18, 19日</td>
    <td class="tg-v16d">1. 方法论简介 <br>2. Python和相关库介绍 </td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2025/lec1/lec1.zip" target="_blank" rel="noopener noreferrer">lec1.zip</a>
    <br>
    <a href="https://nankai.feishu.cn/minutes/obcns72ypxsgqt9iugm89hq9?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-1]</a>
    </td>
    <td class="tg-v16d">
    <a href="https://www.liaoxuefeng.com/wiki/1016959663602400" target="_blank" rel="noopener noreferrer">廖雪峰的Python教程</a>
    </td>
    <td class="tg-v16d"></td>
  </tr>
  <tr>
    <td class="tg-65iu">2</td>
    <td class="tg-65iu">2月25, 26日</td>
    <td class="tg-65iu">1. Python 介绍 <br> 2. 量化平台（优矿）介绍  </td>
    <td class="tg-65iu">
      <a href="/assets/courses/quant_2025/lec2/lec2.zip" target="_blank" rel="noopener noreferrer">lec2.zip</a> <br>
      <a href="https://nankai.feishu.cn/file/FAzXbMtEDo8zv6xpWCzcpdGmnlh" target="_blank" rel="noopener noreferrer">数据：stk_df_2015_2021.zip</a> <br>
      <a href="https://nankai.feishu.cn/minutes/obcnxzth348q11595elg3257?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-2]</a>
    </td>
    <td class="tg-65iu">
    </td>
    <td class="tg-65iu">
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">3</td>
    <td class="tg-v16d">3月4, 5日 </td>
    <td class="tg-v16d">1. 探索数据  <br>
        2. 因子模型 </td>
    <td class="tg-v16d">
      <a href="/assets/courses/quant_2025/lec3/lec3.zip" target="_blank" rel="noopener noreferrer">lec3.zip</a> <br>
      <a href="https://nankai.feishu.cn/file/AaxRbBHc4oCUWZxZ4dvc2bNPnle?from=from_copylink" target="_blank" rel="noopener noreferrer">stk_df.pkl</a> <br>
      <a href="https://nankai.feishu.cn/minutes/obcn3s1b4i7u713i9h4w57v8?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-3]</a>
    </td>
    <td class="tg-v16d">
    </td>
    <td class="tg-v16d">
      <a href="/assets/courses/quant_2025/exercises/ex1.pdf" target="_blank" rel="noopener noreferrer">ex1.pdf</a> <br>
      此日期前提交: 2025.03.19
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">4</td>
    <td class="tg-v16d">3月11,12日 </td>
    <td class="tg-v16d">
        因子模型及相关计量经济学概述 </td>
    <td class="tg-v16d">
      <a href="/assets/courses/quant_2025/lec4/因子模型及相关计量经济学概述.pdf" target="_blank" rel="noopener noreferrer">因子模型及相关计量经济学概述.pdf</a> <br>
      <a href="https://nankai.feishu.cn/minutes/obcn8lst14r156c8krge1gvm?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-4]</a>
    </td>
    <td class="tg-v16d">
      Cochrane (2005), Ch. 12 <br>
      石川, 刘洋溢, & 连祥斌. (2020). 因子投资：方法与实践, Ch. 2
    </td>
    <td class="tg-v16d">
    </td>
  </tr>
  <tr>
    <td class="tg-65iu">5</td>
    <td class="tg-65iu">3月18，19日 </td>
    <td class="tg-65iu"> 排序法：Beta 和 市值  </td>
    <td class="tg-65iu">
      <a href="/assets/courses/quant_2025/lec5/lec5.zip" target="_blank" rel="noopener noreferrer">lec5.zip</a> <br>
      <a href="https://nankai.feishu.cn/file/L4Bqbsvz8o2FATxVarmcSpeOnIh?from=from_copylink" target="_blank" rel="noopener noreferrer">lec5_data.zip</a> <br>
      <a href="https://nankai.feishu.cn/minutes/obcnde7h64gsztk6g7gcn335?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-5]</a>
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
    <td class="tg-v16d">6</td>
    <td class="tg-v16d">3月25，26日</td>
    <td class="tg-v16d"> Fama-French 三因子 </td>
    <td class="tg-v16d">
      <a href="/assets/courses/quant_2025/lec6/lec6.zip" target="_blank" rel="noopener noreferrer">lec6.zip</a> <br>
      <a href="https://nankai.feishu.cn/file/GUPobDpjdoBk2yx4dVvcV7JIn9g?from=from_copylink" target="_blank" rel="noopener noreferrer">FF3_data.zip</a> <br>
      <a href="https://nankai.feishu.cn/minutes/obcnh777y498f2zk174mg472?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-6]</a>
    </td>
    <td class="tg-v16d">
    </td>
    <td class="tg-v16d">
    </td>
  </tr>
  <tr>
    <td class="tg-65iu">7</td>
    <td class="tg-65iu">4月8，9日</td>
    <td class="tg-65iu">
    动量、反转、流动性、波动率因子；回测 <br>
    </td>
    <td class="tg-65iu">
        已更新。前两次课件对应错误也已更新。 <br>
        <a href="/assets/courses/quant_2025/lec7/lec7.zip" target="_blank" rel="noopener noreferrer">lec7.zip</a> <br>
        <a href="https://nankai.feishu.cn/file/X7kKbgiUGoqMx2x7149cprfrngh?from=from_copylink" target="_blank" rel="noopener noreferrer">lec7_data.zip</a> <br>
        <a href="https://nankai.feishu.cn/file/QHkYbXNaQoiDLgxVT7jcTnKRnDb?from=from_copylink" target="_blank" rel="noopener noreferrer">factor_exposure.zip</a> <br>
        <a href="https://nankai.feishu.cn/minutes/obcnrei3pp91972a244j6v47?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-7]</a>
    </td>
    <td class="tg-65iu">
    参考文献见课件
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2025/exercises/ex2.pdf" target="_blank" rel="noopener noreferrer">ex2.pdf</a> <br>
      此日期前提交: 2025.04.23
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">8</td>
    <td class="tg-v16d">4月15，16日 </td>
    <td class="tg-v16d">
    1. 因子模型的应用 <br>
    2. 技术分析介绍和相关的计量经济学
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2025/lec8/bootstrap.zip" target="_blank" rel="noopener noreferrer">bootstrap.zip</a> <br>
    <a href="/assets/courses/quant_2025/lec8/factor_application.zip" target="_blank" rel="noopener noreferrer">factor_application.zip</a> <br>
    <a href="/assets/courses/quant_2025/lec8/ta_test.zip" target="_blank" rel="noopener noreferrer">ta_test.zip</a> <br>
    <a href="https://nankai.feishu.cn/file/J6ceb8hVNoNWqMxZrRocWYplnxg?from=from_copylink" target="_blank" rel="noopener noreferrer">stk_df_ta.zip</a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcnwlm76dt838797enhemiy?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-8]</a> <br>
    </td>
    <td class="tg-v16d">
    参考文献见课件中所列
    </td>
    <td class="tg-v16d">
    </td>
  </tr>
  <tr>
    <td class="tg-65iu">9</td>
    <td class="tg-65iu">4月22，23日</td>
    <td class="tg-65iu">
    技术指标的量化分析 <br>
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2025/lec8/ta_test.zip" target="_blank" rel="noopener noreferrer">ta_test.zip</a> <br>
    <a href="/assets/courses/quant_2025/lec9/7-crs_timing.zip" target="_blank" rel="noopener noreferrer">7-crs_timing.zip</a> 
    <a href="https://nankai.feishu.cn/minutes/obcn2e39cn3vx7497mky2kxj?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-9]</a>
    </td>
    <td class="tg-65iu">
    参考文献见课件中所列
    </td>
    <td class="tg-65iu">
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">10</td>
    <td class="tg-v16d">4月29、30日</td>
    <td class="tg-v16d">
    实践导向的机器学习入门 <br>
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/quant_2025/lec10/ML.pdf" target="_blank" rel="noopener noreferrer">ML.pdf</a> <br>
    <a href="/assets/courses/quant_2025/lec10/entropy.pdf" target="_blank" rel="noopener noreferrer">entropy.pdf</a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcn6781u221996628ao3ehh?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-10]</a>
    </td>
    <td class="tg-v16d">
    </td>
    <td class="tg-v16d"> </td>
  </tr>
  <tr>
    <td class="tg-65iu">11</td>
    <td class="tg-65iu">5月6、7日</td>
    <td class="tg-65iu">
    机器学习应用
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/quant_2025/lec10/ML.pdf" target="_blank" rel="noopener noreferrer">ML.pdf</a> <br>
    <a href="/assets/courses/quant_2025/lec11/approx_NN.ipynb" target="_blank" rel="noopener noreferrer">approx_NN.ipynb</a> <br>
    <a href="/assets/courses/quant_2025/lec11/8-ML.zip" target="_blank" rel="noopener noreferrer">8-ML.zip</a> <br>
    <a href="/assets/courses/quant_2024/lec11/吴 et al-机器学习视角下中国股票资产收益率可预测性研究.pdf" target="_blank" rel="noopener noreferrer">吴 et al-机器学习视角下中国股票资产收益率可预测性研究.pdf</a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcnbzrbvhl42oc93iqp6224?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-11]</a> 
    </td>
    <td class="tg-65iu">
    <a href="https://academic.oup.com/rfs/article/33/5/2223/5758276?login=false" target="_blank" rel="noopener noreferrer">Gu et al. (2020) </a> <br>
    <a href="https://www.sciencedirect.com/science/article/pii/S0304405X21003743" target="_blank" rel="noopener noreferrer">Leippold (2021) </a>
    </td>
    <td class="tg-65iu"> 
    <a href="/assets/courses/quant_2025/exam.pdf" target="_blank" rel="noopener noreferrer">exam.pdf</a> <br>
    请于2025.06.30日前提交
    </td>
  </tr>
  <tr>
    <td class="tg-65iu">12</td>
    <td class="tg-65iu"> 暂定：5月29日 </td>
    <td class="tg-65iu">
    讲座
    </td>
    <td class="tg-65iu">
    </td>
    <td class="tg-65iu">
    </td>
    <td class="tg-65iu"> </td>
  </tr>
</tbody>
</table>


-----
[Back to top](#)