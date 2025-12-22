---
layout: page
title: 计量经济学 I (2025)
description: 
img: assets/img/econometrics_ug.png
importance: 1
category: Earlier
giscus_comments: true
---

# ❗️通知❗️

❗️❗️❗️：中文版公用课件有一些错误。自学请务必以上课时讲解为准。
- 🎉🎉讲座：《逆向思维在投资和就业上的应用》。嘉宾：翟效华，曾任东方财富证券副总经理，资产管理部总监。**时间：5月29日下午3点**。地点：金融学院203。[回放](https://nankai.feishu.cn/minutes/obcnra7s5uf754fg3i9ypl4i?from=from_copylink)
- **2025年5月28日：[作业4](/assets/courses/econometrics_ug/ex4.pdf) 已布置。请于2025年6月11日前提交至助教谢佳桐邮箱：2210968@mail.nankai.edu.cn**
- **2025年5月7日：[作业3](/assets/courses/econometrics_ug/ex3.pdf) 已布置。请于2025年5月22日前提交至助教谢佳桐邮箱：2210968@mail.nankai.edu.cn**
- **2025年4月9日：[作业2](/assets/courses/econometrics_ug/ex2.pdf) 已布置。请于2025年4月24日前提交至助教谢佳桐邮箱：2210968@mail.nankai.edu.cn**
- **2025年3月5日：[作业1](/assets/courses/econometrics_ug/ex1.pdf) 已布置。请于2025年3月20日前提交至助教谢佳桐邮箱：2210968@mail.nankai.edu.cn**

# 1. 课程大纲

<details markdown="1">
  <summary> 详细内容 </summary>

这门课是计量经济学入门。本课程旨在帮助学生掌握使用统计方法分析经济数据的基本技能。课程内容涵盖经济学理论与实际数据之间的关系，重点介绍如何运用回归分析、假设检验等基本计量方法来理解经济现象。学生将学习如何构建和估计经济模型，分析经济变量之间的关系，检验模型的有效性。课程主要内容如下：

- 计量经济学方法论、简史
- 线性回归模型：单变量
- 线性回归模型：多变量
  - 模型估计
  - 统计推断
  - 大样本性质
  - 数据选择、函数形式选择
- 二值变量模型
- 异方差、自相关问题
- 工具变量法

如果时间允许，我将做一些扩展讨论，并简单介绍如何使用软件（如Stata、R、Python等）进行数据分析（AI时代这些变得更容易了）。考试内容将和其他班级统一。

## 教科书

伍尔德里奇 (2016). 计量经济学导论：现代观点（第6版）Wooldridge, J. M. (2016). 

Introductory econometrics: A modern approach (6th ed.). Cengage Learning.

参考书:
- 墙裂推荐 (简称AGE)：Kennedy, Peter (2008). A Guide to Econometrics. 6 edition. Malden, MA: Wiley-Blackwell
- Hayashi, F. (2000). Econometrics. Princeton University Press.
- Wooldridge, J. M. (2010). Econometric Analysis of Cross Section and Panel Data, 2nd ed.
- Angrist, J. D., and J. Pischke, 2009, Mostly Harmless Econometrics: An Empiricist's Companion. 1 edition. (Princeton University Press).

## 评分
- 5次作业, 30%
- 期末考试, 70%


**PLAGIARISM IS STRICTLY PROHIBITED. You may immediately fail the course if copy-pasting other's work.** Discussion is, of course, permitted.

**抄袭作业零容忍。抄袭他人作业可能会直接挂科。** 讨论、交流没有问题，但仍需自己完成。

</details>


# 2. 课程内容
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
<col style="width: 70px">
<col style="width: 190px">
<col style="width: 180px">
<col style="width: 120px">
<col style="width: 80px">
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
    <td class="tg-v16d">2月19日</td>
    <td class="tg-v16d"> 计量经济学方法论、简史 </td>
    <td class="tg-v16d">
    <a href="/assets/courses/econometrics_ug/lec1.zip" target="_blank" rel="noopener noreferrer">lec1.zip </a>
    <br>
    <a href="https://nankai.feishu.cn/minutes/obcnthb369h1bh4p5b3kye49?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-1] </a>
    </td>
    <td class="tg-v16d">
      课本第1章 <br>
      AGE Ch.1, Appendix A
    </td>
    <td class="tg-v16d"></td>
  </tr>
  <tr>
    <td class="tg-65iu">2</td>
    <td class="tg-65iu">2月26日</td>
    <td class="tg-65iu"> 线性回归模型：单变量 </td>
    <td class="tg-65iu">
    <a href="/assets/courses/econometrics_ug/Chapter2.pdf" target="_blank" rel="noopener noreferrer">Ch2.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/Ch2_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch2_课件笔记.pdf </a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcnya21q76o6wf718953bh8?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-2] </a>
    </td>
    <td class="tg-65iu">
    课本第2章 <br> 附录A、B、C
    </td>
    <td class="tg-65iu">
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">3</td>
    <td class="tg-v16d">3月5日</td>
    <td class="tg-v16d"> 1. 线性回归模型：单变量 <br> 2. 线性回归模型：多变量 </td>
    <td class="tg-v16d">
      <a href="/assets/courses/econometrics_ug/Ch2_课件笔记(完整).pdf" target="_blank" rel="noopener noreferrer">Ch2_课件笔记(完整) </a> <br>
      <a href="/assets/courses/econometrics_ug/Ch2_书上笔记.pdf" target="_blank" rel="noopener noreferrer">Ch2_书上笔记.pdf </a> <br>
      <a href="/assets/courses/econometrics_ug/Ch3_0305_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch3_0305_课件笔记.pdf </a> <br>
      <a href="https://nankai.feishu.cn/minutes/obcn332pc2x4z4z233by68r3?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-3] </a>
    </td>
    <td class="tg-v16d">
      课本第3章 <br>
      附录D、E
    </td>
    <td class="tg-v16d">
      <a href="/assets/courses/econometrics_ug/ex1.pdf" target="_blank" rel="noopener noreferrer">ex1.pdf </a> <br>
      提交截止时间：2025年3月20日 <br>
      助教谢佳桐邮箱：2210968@mail.nankai.edu.cn
    </td>
  </tr>
  <tr>
    <td class="tg-65iu">4</td>
    <td class="tg-65iu">3月12日</td>
    <td class="tg-65iu"> 线性回归模型：多变量估计 </td>
    <td class="tg-65iu">
      <a href="/assets/courses/econometrics_ug/Ch3_0312_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch3_0312_课件笔记.pdf </a> <br>
      <a href="https://nankai.feishu.cn/minutes/obcn8v136689v4lhijan7p91?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-4] </a>
    </td>
    <td class="tg-65iu">
      课本第3章
    </td>
    <td class="tg-65iu">
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">5</td>
    <td class="tg-v16d">3月19日 </td>
    <td class="tg-v16d"> 线性回归模型：多变量估计 </td>
    <td class="tg-v16d">
      <a href="/assets/courses/econometrics_ug/Ch3_0319_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch3_0319_课件笔记.pdf </a> （已添加黑板内容） <br>
      <a href="https://nankai.feishu.cn/minutes/obcndoah5z89tbhzks1c3zuc?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-5] </a>
    </td>
    <td class="tg-v16d">
      课本第3章 <br> 附录E
    </td>
    <td class="tg-v16d">
    </td>
  </tr>
  <tr>
    <td class="tg-65iu">6</td>
    <td class="tg-65iu">3月26日 </td>
    <td class="tg-65iu"> 线性回归模型：统计推断 </td>
    <td class="tg-65iu">
      <a href="/assets/courses/econometrics_ug/Ch4.pdf" target="_blank" rel="noopener noreferrer">Ch4.pdf </a> <br>
      <a href="/assets/courses/econometrics_ug/Ch4_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch4_课件笔记.pdf </a> <br>
      <a href="https://nankai.feishu.cn/minutes/obcnih643ebe19o233h18646?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-6] </a> 
    </td>
    <td class="tg-65iu">
      课本第4章 <br>
      附录E
    </td>
    <td class="tg-65iu">
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">7</td>
    <td class="tg-v16d">4月9日 </td>
    <td class="tg-v16d"> 线性回归模型：大样本性质 </td>
    <td class="tg-v16d">
    <a href="/assets/courses/econometrics_ug/Ch5.pdf" target="_blank" rel="noopener noreferrer">Ch5.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/Ch5_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch5_课件笔记.pdf </a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcnr3pb7y477b56t1g326u1?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-7] </a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcnr56j1118o16cum6n1j8j?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-7 作业] </a>
    </td>
    <td class="tg-v16d">
    课本第5章
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/econometrics_ug/ex2.pdf" target="_blank" rel="noopener noreferrer">ex2.pdf </a> <br>
    提交截止时间：2025年4月24日 <br>
      助教谢佳桐邮箱：2210968@mail.nankai.edu.cn
    </td>
  </tr>
  <tr>
    <td class="tg-65iu">8</td>
    <td class="tg-65iu">4月16日 </td>
    <td class="tg-65iu">
    数据选择、函数形式选择 
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/econometrics_ug/Ch6.pdf" target="_blank" rel="noopener noreferrer">Ch6.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/Ch6_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch6_课件笔记.pdf </a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcnwyjdp132s3x8um5iortq?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-8] </a>
    </td>
    <td class="tg-65iu">
    课本第6章
    </td>
    <td class="tg-65iu">
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">9</td>
    <td class="tg-v16d">4月23日</td>
    <td class="tg-v16d">
    1. 二值变量模型 <br>
    2. 自举法 Bootstrap
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/econometrics_ug/Ch7.pdf" target="_blank" rel="noopener noreferrer">Ch7.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/Ch7_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch7_课件笔记.pdf </a> <br>
    <a href="/assets/courses/quant_2025/lec8/bootstrap.zip" target="_blank" rel="noopener noreferrer">bootstrap.zip</a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcn2o2g1ux1a7jyweac8p64?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-9]</a> 
    </td>
    <td class="tg-v16d">
    课本第7章 <br>
    课本第6章附录 <br>
    <a href="https://link.springer.com/chapter/10.1007/978-1-4612-4380-9_41" target="_blank" rel="noopener noreferrer">Efron (1979), Bootstrap</a> 
    </td>
    <td class="tg-v16d"> </td>
  </tr>
  <tr>
    <td class="tg-65iu">10</td>
    <td class="tg-65iu">4月30日</td>
    <td class="tg-65iu">
    异方差
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/econometrics_ug/Ch8.pdf" target="_blank" rel="noopener noreferrer">Ch8.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/Ch8_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch8_课件笔记.pdf </a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcn7h668j4dz46nsavy82a9?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-10]</a>
    </td>
    <td class="tg-65iu">
    课本第8章 <br>
    <a href="https://www.jstor.org/stable/1912934" target="_blank" rel="noopener noreferrer">White (1980)</a>
    </td>
    <td class="tg-65iu"> </td>
  </tr>
  <tr>
    <td class="tg-v16d">11</td>
    <td class="tg-v16d">5月7日</td>
    <td class="tg-v16d">
    自相关，工具变量法（来源）
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/econometrics_ug/Newey_West.pdf" target="_blank" rel="noopener noreferrer">Newey_West.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/Ch15.pdf" target="_blank" rel="noopener noreferrer">Ch15.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/Ch15_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch15_课件笔记.pdf </a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcnca9udn6v6by4ei71ty23?from=from_copylink" rel="noopener noreferrer"> [Video-11] </a> 
    </td>
    <td class="tg-v16d">
    课本第15章 <br>
    <a href="https://www.jstor.org/stable/1913610" rel="noopener noreferrer"> Newey and West (1987) </a> 
    </td>
    <td class="tg-v16d"> 
    <a href="/assets/courses/econometrics_ug/ex3.pdf" target="_blank" rel="noopener noreferrer">ex3.pdf </a> <br>
    提交截止时间：2025年5月22日 <br>
      助教谢佳桐邮箱：2210968@mail.nankai.edu.cn
    </td>
  </tr>
  <tr>
    <td class="tg-65iu">12</td>
    <td class="tg-65iu">5月14日</td>
    <td class="tg-65iu">
    工具变量法（性质）
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/econometrics_ug/Ch15.pdf" target="_blank" rel="noopener noreferrer">Ch15.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/Ch15_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch15_课件笔记.pdf </a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcng4347ulz9u9e26vs53hj?from=from_copylink" rel="noopener noreferrer"> [Video-12] (第一段缺失) </a> 
    </td>
    <td class="tg-65iu">
    </td>
    <td class="tg-65iu"> </td>
  </tr>
  <tr>
    <td class="tg-v16d">13</td>
    <td class="tg-v16d">5月21日</td>
    <td class="tg-v16d">
    工具变量法（检验、应用）
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/econometrics_ug/Ch15.pdf" target="_blank" rel="noopener noreferrer">Ch15.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/Ch15_课件笔记.pdf" target="_blank" rel="noopener noreferrer">Ch15_课件笔记.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/IV_Griliches.zip" target="_blank" rel="noopener noreferrer">IV_Griliches.zip</a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcnlv529744529kshg4lud7?from=from_copylink" rel="noopener noreferrer"> [Video-13] </a> 
    </td>
    <td class="tg-v16d">
    </td>
    <td class="tg-v16d"> </td>
  </tr>
  <tr>
    <td class="tg-65iu">14</td>
    <td class="tg-65iu">5月28日</td>
    <td class="tg-65iu">
    工具变量法、GMM
    </td>
    <td class="tg-65iu">
    <a href="/assets/courses/econometrics_ug/GMM.pdf" target="_blank" rel="noopener noreferrer">GMM.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/GMM_课件笔记.pdf" target="_blank" rel="noopener noreferrer">GMM_课件笔记.pdf </a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcnqs2vz5suq5s4y94oyi5i?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-14]</a>
    </td>
    <td class="tg-65iu">
    <a href="https://www.aeaweb.org/articles?id=10.1257%2Faer.91.5.1369&ref=marionomics-economia-y-ciencia-de-datos" rel="noopener noreferrer"> Acemoglu, Johnson, Robinson (2001) </a> 
    </td>
    <td class="tg-65iu"> 
    <a href="/assets/courses/econometrics_ug/ex4.pdf" target="_blank" rel="noopener noreferrer">ex4.pdf </a> <br>
    提交截止时间：2025年6月11日 <br>
      助教谢佳桐邮箱：2210968@mail.nankai.edu.cn
    </td>
  </tr>
  <tr>
    <td class="tg-v16d">15</td>
    <td class="tg-v16d">6月4日</td>
    <td class="tg-v16d">
    Rubin因果模型；联立方程简介；方法论回顾
    </td>
    <td class="tg-v16d">
    <a href="/assets/courses/econometrics_ug/Rubin's causal model.pdf" target="_blank" rel="noopener noreferrer">Rubin.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/第24章-联立方程模型 pages 1 - 14.pdf" target="_blank" rel="noopener noreferrer">联立方程.pdf </a> <br>
    <a href="/assets/courses/econometrics_ug/方法论回顾.pdf" target="_blank" rel="noopener noreferrer">计量经济学方法论回顾.pdf </a> <br>
    <a href="https://nankai.feishu.cn/minutes/obcnvh1g5sgximw14c21m2dr?from=from_copylink" target="_blank" rel="noopener noreferrer">[Video-15]</a>
    </td>
    <td class="tg-v16d">
    </td>
    <td class="tg-v16d"> </td>
  </tr>
  <tr>
    <td class="tg-65iu">16</td>
    <td class="tg-65iu">6月11日</td>
    <td class="tg-65iu">
    课程回顾、习题解答
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