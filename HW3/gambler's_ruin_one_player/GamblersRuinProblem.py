import random
import matplotlib.pyplot as plt

# 證明 P(up k before down n) = n / (n + k)
# 資產到 (n + k) 或是 0, 遊戲便停止

# 起始資金(n)
n = 100

# 需要贏得多少錢才算獲勝(k)
k = 200

# 模擬次數
times = 10000

# Player 1 獲勝的機率
p = 0.5

# 紀錄輸贏次數
wins = 0
loses = 0

for _ in range(times):
    
    balance = n

    while balance < (n + k) and balance > 0 :

        if random.random() < p:
            balance += 1
        else:
            balance -= 1

    # 在結束時紀錄誰贏了
    if balance == (n + k):
        wins += 1
    else:
        loses += 1

print("player 1 win", wins, "times")
print("player 1 lose", loses, "times")
print("P(up k before down n) =", wins / times)

# 作圖
labels = ['Player 1 Wins', 'Player 1 Loses']
values = [wins, loses]

plt.bar(labels, values)
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.title(f"Gambler's Ruin Simulation (Simulations: {times})")
plt.show()