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

## Task Assignment
1. ✅ Generate Test Data
2. ✅ File Reading:
    - `get_school_data()`
    - `get_student_data()`
3. Distribution Algorithm
4. Distribution Algorithm Optimization
5. Validation
6. Visual Analysis
7. Report

## Contributors
- 電資二 110820012 宋典諺
- 電資二 110820040 蔡宇倫
- 電資二 110820058 萬祥瑞
- 電資二 110820059 林于喬

## Reference
- [大學聯考分發程式及其相關問題探討](http://ip194097.ntcu.edu.tw/ungian/Chokphin/Hoagu/hunhoat/hunhoat.htm)
- [【電機專題】指考將至 你知道考試是怎麼分發的嗎 | 15分鐘搞定分發問題的演算法與資料結構！](https://youtu.be/Ss4w4jghqXc)
- [Data-Structure-Final-Project](https://github.com/H-Scorpion/Data-Structure-Final-Project)
- [中文姓名產生器 v3.4](http://www.richyli.com/name/index.asp)

## TestCase
```python
['台灣大學', '醫學系', '1001', 2]
['台灣大學', '電機系', '1002', 3]
['清華大學', '化學系', '2004', 2]
['清華大學', '數學系', '2008', 4]
['政治大學', '外交系', '3009', 2]
```
```python
['11080002', '楊順亦', '2004', 0, '2008', 0, '1002', 3, 'None', 'None', 'None', 'None', 'None', 'None']
['11080003', '劉雅書', '1001', 0, '1002', 0, '2008', 0, 'None', 'None', 'None', 'None', 'None', 'None']
['11080004', '郭姵紫', '2004', 1, '3009', 0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
['11080005', '陳怡喬', '2008', 3, '2004', 2, '3009', 1, 'None', 'None', 'None', 'None', 'None', 'None']
['11080006', '林宜禾', '2008', 0, '1001', 1, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
['11080007', '曹昀志', '3009', 2, '1002', 2, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
['11080008', '李偉昀', '3009', 0, '2004', 3, '2008', 2, 'None', 'None', 'None', 'None', 'None', 'None']
['11080009', '陳雅玲', '1002', 0, '2004', 0, '2008', 0, 'None', 'None', 'None', 'None', 'None', 'None']
['11080010', '陳建緯', '2008', 4, '3009', 3, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
['11080011', '毛雲誠', '1001', 2, '1002', 1, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
['11080012', '許俊玲', '2008', 1, '1002', 0, '1001', 3, 'None', 'None', 'None', 'None', 'None', 'None']
['11080013', '王梅智', '2004', 4, '3009', 4, '1001', 0, 'None', 'None', 'None', 'None', 'None', 'None']
['11080014', '林佳蓉', '2004', 5, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
```