# 2023 Computer Algorithms Final Project
**Exploring the Algorithm and Complexity of the Individual Application Centralized Distribution System in Taiwan's Education System**

## Motivation
Our motivation is to improve the waiting time for students during the process of filling out their school preferences and allocation. The current procedure includes completing GSAT(General Scholastic Ability Test), waiting for the results to be announced, submitting preference schools, providing written review materials, waiting for the results of the initial screening, attending interviews with various schools, waiting for the announcement of waitlist results, and finally, allocation. There are long intervals between each step, which can make students feel impatient and restless. Therefore, we hope to implement an algorithm to reduce the waiting time in certain stages.
## Expected goals
After the announcement of the results of the second-stage interviews, students will be able to find out if they have been offered a spot in the regular admission or the waitlist. Then, they can submit their preference order for the schools they wish to attend. Once we have obtained the students' preference order, we will first implement a distribution algorithm and then attempt to analyze its complexity to identify if there are any optimization methods available.
## Importance
Firstly, the immediate benefit of this algorithm is that it allows waitlisted students to know if they have the opportunity to enter their desired schools. This way, they can reduce their disappointment. Additionally, this algorithm can also be applied to other types of allocation scenarios. As long as it involves a many-to-one allocation problem, our algorithm can be utilized effectively.

## 統一分發原則：
- 錄取單一校系之錄取生仍須完成就讀志願序登記，正取生確定可分發至該校系；
- 備取生則待該校系正取生分發後之缺額進行遞補分發，若無缺額則不予分發。
- 錄取生如同時錄取多個校系，甄選委員會依其登記就讀志願序進行統一分發
    - 如正取校系志願序於備取校系之前，則取其正取校系最優先志願分發；
    - 如備取校系志願序於正取校系之前，當該備取校系之正取生分發後尚有缺額時，即進行遞補分發；
    - 若該校系分發人數達招生名額，則不予分發至該校系。
- 遇備取名次相同致分發結果超過原招生名額時，則一併增額分發至該校系。
- 增額之名額如屬教育部核定當學年度各系組之新生招生名額者，應由當學年度大學分發入學招生名額調整流用。

## Contributors
- 電資二 110820012 宋典諺
- 電資二 110820040 蔡宇倫
- 電資二 110820058 萬祥瑞
- 電資二 110820059 林于喬

## Gale-Shapley Algorithm
- [Note](./GaleShapleyNote/readme.md)

## Flowchart
![Flowchart](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Algorithm/Flowchart2.png)

## Reference
- [大學聯考分發程式及其相關問題探討](http://ip194097.ntcu.edu.tw/ungian/Chokphin/Hoagu/hunhoat/hunhoat.htm)
- [【電機專題】指考將至 你知道考試是怎麼分發的嗎 | 15分鐘搞定分發問題的演算法與資料結構！](https://youtu.be/Ss4w4jghqXc)
- [婚姻中的賽局理論！從兩首古詩理解「穩定婚姻問題」](https://pansci.asia/archives/330654)
- [14-5: 稳定婚配问题 Stable Marriage Problem](https://www.bilibili.com/video/BV1V44y167n3/?spm_id_from=333.788&vd_source=434422c653cb22ae533f5fa626e984c1)
- [14-6: Gale-Shapley 算法 寻找稳定婚配](https://www.bilibili.com/video/BV1uq4y177Hc/?spm_id_from=333.788&vd_source=434422c653cb22ae533f5fa626e984c1)
- [Economic analysis of Taiwan high school matching system](http://etd.lib.nsysu.edu.tw/ETD-db/ETD-search-c/view_etd?URN=etd-0530116-005800)