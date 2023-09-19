# 隨機過程 HW3 

### 1. Simulate the process of the moving particle until all nodes are visited

以下分別是以 0 為起點, 執行 100, 1000, 10000, 及 100000 次的結果

**100 次**

![100](https://github.com/Frisk0316/Stochastic-Process/assets/79501315/a79dca11-8d4c-4cbd-b06a-3287a1533c82)

**1,000 次**

![1000](https://github.com/Frisk0316/Stochastic-Process/assets/79501315/6cb1e029-22f4-4cb0-aa39-c66dcd42e656)

**10,000 次**

![10000](https://github.com/Frisk0316/Stochastic-Process/assets/79501315/0a99d3bf-bd30-46b2-a9d5-fc5e2c00aa58)

**100,000 次**

![100000](https://github.com/Frisk0316/Stochastic-Process/assets/79501315/0f6534f7-c992-419b-9878-f68e9eb65f90)

隨著次數越多，我們可以發現每個節點為終點的機率越來越趨近於一致，亦即若有 0 ~ n 個節點，並以 0 號做為起點，其餘節點 (1 ~ n) 為終點的機率為 1/n 

### 3. Gambler’s ruin problem

a. 初始雙方本金為 10 元, 模擬一萬次, player_1 與 player_2 贏的機率皆為 0.5

結果：

player 1 win 4950 times

player 2 win 5050 times

![gamblers_ruin_10_10000](https://github.com/Frisk0316/Stochastic-Process/assets/79501315/560c7088-df29-4076-b180-7643c92e1e8d)

b. 初始雙方本金為 100 元, 模擬一萬次, player_1 與 player_2 贏的機率皆為 0.5

結果：

player 1 win 4932 times

player 2 win 5068 times

![gamblers_ruin_100_10000](https://github.com/Frisk0316/Stochastic-Process/assets/79501315/1d68396f-71f7-4f02-bb29-3f37c722ec6a)


c. 初始雙方本金為 10 元, 模擬一萬次, player_1 贏的機率為 0.6, 而 player_2 贏的機率為 0.4

結果：

player 1 win 9836 times

player 2 win 164 times

![gamblers_ruin_10_10000_0 6](https://github.com/Frisk0316/Stochastic-Process/assets/79501315/5862f512-336a-4691-ad35-7bb517d23f03)

d. 初始雙方本金為 100 元, 模擬一萬次, player_1 贏的機率為 0.6, 而 player_2 贏的機率為 0.4

結果：

player 1 win 10000 times

player 2 win 0 times

![gamblers_ruin_100_10000_0 6](https://github.com/Frisk0316/Stochastic-Process/assets/79501315/829a9991-614c-4b5f-a191-8abf84e0d090)
