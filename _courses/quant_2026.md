---
layout: page
title: 量化投资/金融数据分析 (硕士、博士，2026)
description: 因子模型；技术分析的统计检验；机器学习
img: assets/img/quant2025.png
importance: 2
category: 2026
giscus_comments: true
numbering: true
toc:
  sidebar: left
no_number: ["通知"]
---

## ❗️通知❗️
- 2026.03.17: 第一次作业已布置，请于2026年3月31日前提交。助教于谨豪邮箱：2213609@mail.nankai.edu.cn
- 3.3: 课程内容调查问卷：[https://v.wjx.cn/vm/h9eRD9e.aspx#](https://v.wjx.cn/vm/h9eRD9e.aspx#)

## 课程大纲

<!-- &nbsp; -->

 <details markdown="1">
  <summary> 详细内容 Details </summary>

这门课程在教学计划上有两个不同的名称：《量化投资》(学硕)，《金融数据分析和Python应用》(专硕)。主要讨论用数量方法探索金融数据以及构建交易策略。课程内容是应用导向的，但相关的理论也会有涉及。课程目标：掌握基本的工具以及用数据分析的思维方式。这门课主要包含以下内容：
- Python 基础以及数据处理相关库(numpy, pandas, SKlearn, Pytorch等)
- 因子模型
- 回测框架
- 技术分析介绍以及统计检验
- 机器学习和深度学习在量化投资中的应用
- 多工具综合应用

今年的课程将在讲解清楚原理的基础上，进一步探讨AI相关内容的应用。具体内容将根据实际进度和大家的作业完成情况进行调整。

这门课暂不包含高频数据(日内)策略。主要的数据来源是中国A股市场股票数据

### 知识储备
应当知道基本的计量经济学(我们会进行简短的复习)。无需具备编程知识，所有的编程相关的内容都会在课程中介绍，但如果有编程经验更好。面对大量的编程应当有心理准备。

### 课本和参考书
暂无课本。课件和相关资料会上传到这个网页，请每次上课前进行下载。我们采用的平台是[优矿](https://uqer.datayes.com/)，请至相关网页下载客户端。优矿有免费版但分配的计算资源很少，学院会提供一些共享账号。参考书目见下方。

- Cochrane, John H., 2005, *Asset Pricing*. Revised edition. (Princeton University Press, Princeton, N.J).
- Bali, Turan G., Robert F. Engle, and Scott Murray, 2016, *Empirical Asset Pricing: The Cross Section of Stock Returns*. 1 edition. (Wiley).
- 石川, 刘洋溢, & 连祥斌. (2020). 因子投资：方法与实践. 电子工业出版社.
- Murphy, John J., 1999, *Technical Analysis of the Financial Markets: A Comprehensive Guide to Trading Methods and Applications*. (New York Institute of Finance, N.Y.).
- Grinold, Richard, and Ronald Kahn, 1999, *Active Portfolio Management: A Quantitative Approach for Producing Superior Returns and Controlling Risk*. 2 edition. (McGraw-Hill Education, New York).
- Geron, Aurelien, 2021, *Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow*. 3rd Edition (O'Reilly).

### 评分方式
- 3次作业 (70%)
- 开放式项目 (30%)

**抄袭作业零容忍。抄袭他人作业可能会直接挂科。** 对于编程经验较少的同学来说，遇到困难是正常的。所有的代码我都会共享，只要仔细研读一定可以完成作业和考试。请相信自己。

**PLAGIARISM IS STRICTLY PROHIBITED. You may immediately fail the course if copy-pasting other's work.** It will be normal to meet obstacles during the course, especially for students with less exposure to programming. I'll share all relevant code and you'll surely complete the course successfully if you read and try the provided code with some care. Please trust yourself and hang on.

</details>

&nbsp;

## 课程内容

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
      <td>3.3 </td>
      <td>
        1. 课程介绍 <br>
        2. Python 介绍
      </td>
      <td>
      <a href="/assets/courses/quant_2026/Intro.pdf" target="_blank" rel="noopener noreferrer">Intro.pdf</a> <br>
    <a href="/assets/courses/quant_2026/Python_intro.ipynb" target="_blank" rel="noopener noreferrer">Python_intro.ipynb</a> 
      </td>
      <td>
      <a href="https://liaoxuefeng.com/books/python/introduction/index.html">廖雪峰《Python 教程》</a>
      </td>
      <td></td>
    </tr>
        <tr>
      <td>2</td>
      <td>3.10 </td>
      <td>
      1. Python 的金融数据分析简介(pandas, numpy, matplotlib) <br>
      2. 量化回测平台介绍与回测代码构建
      <!-- 专硕讲到回测的基本逻辑，还未看具体代码构建的过程 -->
      <!-- 学硕讲完第一个回测策略，动量策略 -->
      </td>
      <td>
      <a href="/assets/courses/quant_2026/np_pd_plot.ipynb" target="_blank" rel="noopener noreferrer">np_pd_plot.ipynb</a> <br>
      <a href="/assets/courses/quant_2026/strategy_example.ipynb" target="_blank" rel="noopener noreferrer">strategy_example.ipynb</a> 
      </td>
      <td>
      </td>
      <td></td>
    </tr>
        <tr>
      <td>3</td>
      <td> 3.17 </td>
      <td>
        1. 探索数据 <br>
        2. 因子模型和相关计量经济学概述
      </td>
      <td>
      <a href="/assets/courses/quant_2026/1-EDA.ipynb" target="_blank" rel="noopener noreferrer">1-EDA.ipynb</a> <br>
      <a href="/assets/courses/quant_2026/因子模型及相关计量经济学概述.pdf" target="_blank" rel="noopener noreferrer">因子模型讨论</a> <br>
      <a href="https://nankai.feishu.cn/file/LaUybViOwo8D6ex4NWXchKOGnWg?from=from_copylink" target="_blank" rel="noopener noreferrer">stk_df_2025.zip</a>
      </td>
      <td>
      参考文献见课件
      </td>
      <td>
      <a href="https://nankai.feishu.cn/file/Hfg4bG3MloalXdxRHoEcPBClnmh?from=from_copylink" target="_blank" rel="noopener noreferrer">hw1.zip</a> <br>
      此日期前提交: 2025.03.31 <br>
      助教于谨豪邮箱：2213609@mail.nankai.edu.cn
      </td>
    </tr>
        <tr>
      <td>4</td>
      <td> 3.24 </td>
      <td>
       因子模型和相关计量经济学概述
      </td>
      <td>
      </td>
      <td>
      </td>
      <td></td>
    </tr>
        <tr>
      <td>5</td>
      <td>3.31 </td>
      <td>
        因子模型实践：Beta 和 市值
      </td>
      <td>
      </td>
      <td>
      </td>
      <td></td>
    </tr>
        <tr>
      <td>6</td>
      <td>4.7 </td>
      <td>
        Fama-French 三因子
      </td>
      <td>
      </td>
      <td>
      </td>
      <td></td>
    </tr>
        <tr>
      <td>7</td>
      <td>4.14 </td>
      <td>
       3. 动量、反转、流动性、波动率因子 <br>
       4. 量化平台回测
      </td>
      <td>
      </td>
      <td>
      </td>
      <td></td>
    </tr>
        <tr>
      <td>8</td>
      <td>4.21 </td>
      <td>
        5. 因子模型的应用 <br>
        6. 技术分析介绍和相关的统计分析
      </td>
      <td>
      </td>
      <td>
      </td>
      <td></td>
    </tr>
        <tr>
      <td>9</td>
      <td>4.28 </td>
      <td>
        7. 技术分析的量化分析 <br>
        8. 机器学习介绍
      </td>
      <td> 
      </td>
      <td>
      </td>
      <td></td>
    </tr>
        <tr>
      <td>10</td>
      <td>5.5 </td>
      <td>
        量化策略的机器学习应用
      </td>
      <td> 
      </td>
      <td>
      </td>
      <td></td>
    </tr>
        <tr>
      <td>11</td>
      <td>5.12 </td>
      <td>
        量化策略的机器学习应用
      </td>
      <td>
      </td>
      <td>
      </td>
      <td></td>
    </tr>
        <tr>
      <td>12</td>
      <td>待定  </td>
      <td>
        讲座
      </td>
      <td>
      </td>
      <td>
      </td>
      <td></td>
    </tr>
  </tbody>
</table>


-----
[Back to top](#)