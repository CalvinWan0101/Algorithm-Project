# Gale-Shapley 與 Stable Marriage

# Stable Marriage Problem

- [婚姻中的賽局理論！從兩首古詩理解「穩定婚姻問題」](https://pansci.asia/archives/330654)

## 穩定婚姻的例子

### 成員

男：甲、乙、丙

女：A, B, C

### 起始喜好

|  | 順位1 | 順位2 | 順位3 |
| --- | --- | --- | --- |
| A女 | 乙 | 丙 | 甲 |
| B女 | 丙 | 甲 | 乙 |
| C女 | 甲 | 乙 | 丙 |

|  | 順位1 | 順位2 | 順位3 |
| --- | --- | --- | --- |
| 甲男 | A | B | C |
| 乙男 | B | C | A |
| 丙男 | C | A | B |

有六組，但其中三組是穩定婚姻

### 第一組

- 所有的女性都配對到自己最喜歡的男性
- 雖然所有男性都匹配到自己最不喜歡的女性，但沒有女性願意出軌
- 故這個組合是穩定婚姻

|  | 順位1 | 順位2 | 順位3 |
| --- | --- | --- | --- |
| A女 | 乙 | 丙 | 甲 |
| B女 | 丙 | 甲 | 乙 |
| C女 | 甲 | 乙 | 丙 |

|  | 順位1 | 順位2 | 順位3 |
| --- | --- | --- | --- |
| 甲男 | A | B | C |
| 乙男 | B | C | A |
| 丙男 | C | A | B |

### 第二組

- 所有的男性都配對到自己最喜歡的女性
- 雖然所有女性都匹配到自己最不喜歡的男性，但沒有男性願意出軌
- 故這個組合是穩定婚姻

|  | 順位1 | 順位2 | 順位3 |
| --- | --- | --- | --- |
| A女 | 乙 | 丙 | 甲 |
| B女 | 丙 | 甲 | 乙 |
| C女 | 甲 | 乙 | 丙 |

|  | 順位1 | 順位2 | 順位3 |
| --- | --- | --- | --- |
| 甲男 | A | B | C |
| 乙男 | B | C | A |
| 丙男 | C | A | B |

### 第三組

- 雖然不論男女都只匹配到自己第二喜歡的異性
- 如果有人不知足，想找自己的順位1
- 自己的順位1看不上自己

|  | 順位1 | 順位2 | 順位3 |
| --- | --- | --- | --- |
| A女 | 乙 | 丙 | 甲 |
| B女 | 丙 | 甲 | 乙 |
| C女 | 甲 | 乙 | 丙 |

|  | 順位1 | 順位2 | 順位3 |
| --- | --- | --- | --- |
| 甲男 | A | B | C |
| 乙男 | B | C | A |
| 丙男 | C | A | B |

## 結論

從這個例子可以看出：**穩定婚姻的演算法並不保證唯一解，而且也不保證人人都美滿幸福。**

# Gale-Shapley

**小紅書搜推算法工程師的講解**

- [稳定婚配问题 Stable Marriage Problem](https://www.bilibili.com/video/BV1V44y167n3/?spm_id_from=333.788&vd_source=434422c653cb22ae533f5fa626e984c1)
- [Gale-Shapley 算法 寻找稳定婚配](https://www.bilibili.com/video/BV1uq4y177Hc/?spm_id_from=333.788&vd_source=434422c653cb22ae533f5fa626e984c1)

**主要精神**

- 男生可以挖墻腳
- 男生不能吃回頭草
- 女生可以騎驢找馬

## Gale-Shapley Algorithm

### 中心思想

1. Every unmarried man proposes to a woman who is his most preferred among those he has not proposed to.
2. A woman marries her most preferred suitor.
    - A bad suitor is better than no suitor.
    - If the suitor is better than her current husband, then she will divorce.
3. Stop if everyone is married; otherwise, repeat Step 1 and 2

### 說人話

1. 每個單身男向他最喜歡的女生求婚
    - 可以是已婚女
    - 不能是以前求婚過的
2. 女性來決定接受誰的求婚
    - 一個人求婚 ⇒ 接受求婚
    - 多個人求婚 ⇒ 接受最喜歡的人的求婚
    - 已婚 ⇒ 比較求婚者與丈夫的優先序列
3. 如果所有人都結婚了 ⇒ 終結程式
4. 否則 ⇒ 重複 Step 1 與 Step 2

### Time Complexity:

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled.png)

## Example 1. 三男三女

### Input

喜好排序

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%201.png)

### Iteration 1

- 每個男生都向自己最喜歡的女生求婚
- 允許兩個以上的男生向同一個女生求婚
- 不能向同一個女生女生求婚兩次

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%202.png)

- 只有 Bob 向 Becky ⇒ Becky 與 Bob結婚
- Alex 與 Chris 同時向 Ada 求婚
    - Ada 選擇優先序位較高的 Alex
    - Chris 孤家寡人接受下一輪分發

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%203.png)

- 如果一個已婚的女生被另外一個男生求婚
    - 判斷這個男生是否比自己的老公好
        - 若是好 ⇒ 則把老公換掉
        - 若是不好 ⇒ 則拒絕

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%204.png)

### Iteration 2

- Chris 向已婚的 Becky 求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%205.png)

- Becky 判斷 Chris 的優先級是否高於 Bob
- 是 ⇒ Becky 拒絕求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%206.png)

### Iteration 3

- Chris 向 Cindy 求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%207.png)

- Cindy 接受

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%208.png)

### End of Procedure

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%209.png)

## Example 2. 四男四女

### Input

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2010.png)

### Iteration 1

- 每個男生都向自己最喜歡的女生求婚
- 允許兩個以上的男生向同一個女生求婚
- 不能向同一個女生女生求婚兩次

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2011.png)

- 只有 Chris 向 Becky 求婚 ⇒ 結婚
- 只有 David 向 Cindy 求婚 ⇒ 結婚
- Alex 同時與 Bob 向 Ada 求婚
    - Alex 優先級比 Bob 高 ⇒ Ada 與 Alex 結婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2012.png)

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2013.png)

### Iteration 2

- Bob 向已婚的 Becky 求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2014.png)

- Becky 更喜歡老公 Chris
- 拒絕求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2015.png)

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2016.png)

### Iteration 3

- Bob 向已婚的 Cindy 求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2017.png)

- Cindy 更喜歡 Bob
- Cindy 與 Bob 結婚
- Cindy 與老公 David 離婚
- David 成為綠帽俠

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2018.png)

- 現在 David 單身

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2019.png)

### Iteration 4

- David 向已婚的 Ada 求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2020.png)

- Ada 更喜歡老公 Alex
- 拒絕求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2021.png)

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2022.png)

### Iteration 5

- David 向已婚的 Becky 求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2023.png)

- Becky 比起老公 Chris 她更喜歡 David
- Becky 與老公 Chris 離婚
- Becky 與 David 結婚
- Chris 成為綠帽俠

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2024.png)

- 現在 Chris 單身

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2025.png)

### Iteration 6

- Chris 向 Diana 求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2026.png)

- 雖然 Diana 不喜歡 Chris，但她還是接受了 Chris 的求婚

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2027.png)

### End of Procedure

![Untitled](https://raw.githubusercontent.com/CalvinWan0101/Algorithm-Project/main/Gale_Shapley_Note/img/Untitled%2028.png)