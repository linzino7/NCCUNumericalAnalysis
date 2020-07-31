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
