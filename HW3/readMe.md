# 隨機過程 HW3 
## r12723071 陳芃

### 1. Simulate the process of the moving particle until all nodes are visited

以下分別是以 0 為起點, 執行 100, 1000, 10000, 及 100000 次的結果

**100 次**
![image](D:\台大財金所\碩一上\隨機過程\HW3\HW3 r12723071\100.png)

**1,000 次**
**10,000 次**
**100,000 次**


執行程式碼如下:

```
import random
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# 定義變數
nodes = 10
times = 100

# 定義所有最終被造訪的節點起始次數為 0 (0 ~ nodes)
last_visited_counts = [0] * (nodes + 1)

for _ in range(times):

    # 將造訪的節點納入不重複之集合
    nodes_visited = set()

    # 將起始點新增進 node_visited
    current_node = 0 
    nodes_visited.add(current_node)

    while len(nodes_visited) <= nodes:

        # 決定為 (+1, -1)
        next_node = current_node + random.choice([1, -1])

        # next_node 為 -1 代表跳到最大的 node
        if next_node == -1:
            next_node = nodes
        
        # next_node 大於 nodes 代表跳到 0 
        elif next_node > nodes:
            next_node = 0

        current_node = next_node
        
        # 新增現在的節點
        nodes_visited.add(current_node) 

        # print("current node: ", current_node)
        # print("length of nodes visited: ", len(nodes_visited))

    # last_visited_node = current_node
    last_visited_counts[current_node] += 1

    # print("")
    # print("last visit node is: ", current_node)
    # print("")

# 作圖, 要注意的是共有 n + 1 個 nodes
plt.bar(range(0, nodes + 1), last_visited_counts)
plt.xlabel('Last Visited Node')
plt.ylabel('Frequency')
plt.title(f'Last Visited Node Frequency (Simulations: {times})')
plt.xticks(range(0, nodes + 1))
plt.show()


```