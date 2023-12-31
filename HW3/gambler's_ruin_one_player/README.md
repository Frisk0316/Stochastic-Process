# 3. Gambler's Ruins Problem

### (1) p = q = 0.5

| 模擬次數 (times) | 起始金額 (n) | 需要贏得的金額 (k) | 獲勝機率 (p) | 獲勝次數 (總金額達到 n+k) | 輸掉的次數 (總金額達到 0) | P(up k before down n) | $\frac{n}{n+k}$  |
|---|---|---|---| --- | ---| --- | --- |
| 10,000 | 100 | 10 | 0.5 | 9,115 | 885 | 0.9115 | 0.9091 |
| 10,000 | 100 | 20 | 0.5 | 8,240 | 1,760 | 0.8240 | 0.8333 |
| 10,000 | 100 | 50 | 0.5 | 6,692 | 3,308 | 0.6692 | 0.6667 |
| 10,000 | 100 | 100 | 0.5 | 4,961 | 5,039 | 0.4961 | 0.5000 |
| 10,000 | 100 | 200 | 0.5 | 3,342 | 6,658 | 0.3342 | 0.3333 |

當 p = 0.5, P( up k before down n ) 會趨近於 $\frac{n}{n+k}$

### (2) p = 0.6, q = 0.4

| 模擬次數 (times) | 起始金額 (n) | 需要贏得的金額 (k) | 獲勝機率 (p) | 獲勝次數 (總金額達到 n+k) | 輸掉的次數 (總金額達到 0) | P(up k before down n) | $\frac{n}{n+k}$  |
|---|---|---|---| --- | ---| --- | --- |
| 10,000 | 100 | 20 | 0.6 | 10,000 | 0 | 1.0000 | 0.8333 |
| 10,000 | 100 | 50 | 0.6 | 10,000 | 0 | 1.0000 | 0.6667 |
| 10,000 | 100 | 100 | 0.6 | 10,000 | 0 | 1.0000 | 0.5000 |

當 p = 0.6, P( up k before down n ) = 1
