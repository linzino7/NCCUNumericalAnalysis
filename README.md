# NCCUNumericalAnalysis 2018
本專案專為紀錄政大數學系數值分析上課用程式碼。<br>
使用IDE為Spyder所以會跟上課有所不同。

## 課程連結
http://moocs.nccu.edu.tw/course/132/intro

## 筆記
### Week3 Unit02 Bisection method
exp(x) 微分還是exp(x)。

### Week3 Unit08 newton's method 2nd convergence
幾階收斂就是代表收斂的速度，越大就是越快。只要可以收斂到某個常數C。

### Week3 Unit04 brouwer's fixed point theorem
這裡會可以使用Simple iteration 實做，並不段把 x 帶入y 就會逼緊答案是因為假設：y=g(x),y=x 的關係。

### Week4 Unit3 Gauss elimination
只需要把第一欄資料做排序就可以了。是避免0在最上面。

#### Gauss elimination 流程：
[[ A, 6, 5], <br>
 [ 1, B, 4], <br>
 [ 2, 3, C]] <br>
##### 左下：
  1. 把一列最大值排序到A。
  2. 把1 透過A的 倍數把1歸0。 
  3. 重複上兩個動作做完  2 ,3  （到3 時用B解）。
##### 右上：
  4. 確認C 是否跟後方答案有倍數關係。有就把C 變成1。
  5. 把4 透過C的 倍數把4歸0。因為這時都 2, 3 都會是0 所以使用C來。 5也是用c來解因為這。
  6. 重複上兩個動作做完  4 ,5  （到6 時用B解）。

### Week4 Unit4 LU decomposition

#### LU decomposition 流程：
P,A,L,U皆為n*n的矩陣<br>
P：控制攔列隊調<br>
A：是原始要被解開的矩陣<br>
L：由上角為0的矩陣，且對角線為1。起始值為對角線為1的n*n單位矩陣<br>
U：為左下角0的矩陣。 起始值為A矩陣複製而來。<br>

1. 先判斷對角線下的值是否有比對角線的值還要大。
- 2. 把U大的列調換到對角線。
- 3. 把P大的列調換到對角線。
- 4. 把L先做攔對調，在做列對調。( 因為要把左右的P 都乘到L 中)

6. 在 U 中 遇到非0的值。
- 7. 計算C：要乘幾倍去把0削掉。
- 8. L =  對角線* -C 去減掉非0那一列
- 9. U =  對角線 * C 去減掉非0那一列

重點是讓 PA = LU


