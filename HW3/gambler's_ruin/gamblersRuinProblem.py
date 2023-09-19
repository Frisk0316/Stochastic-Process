import random
import matplotlib.pyplot as plt

# 參數設定
initial_balance = 100
simulations = 10000
results = []

for _ in range(simulations):
    player_1_balance = initial_balance
    player_2_balance = initial_balance

    while player_1_balance > 0 and player_2_balance > 0:
        # Player 1 獲勝的機率 = 0.5
        if random.random() < 0.6:
            player_1_balance += 1
            player_2_balance -= 1
        else:
            player_1_balance -= 1
            player_2_balance += 1

    # Record the result of each simulation
    if player_1_balance == 0:
        results.append(2)  # Player 2 wins
    else:
        results.append(1)  # Player 1 wins

# 計算兩個玩家獲勝的次數
player_1_wins = results.count(1)
player_2_wins = results.count(2)

print("player 1 win", player_1_wins, "times")
print("player 2 win", player_2_wins, "times")

# 作圖
labels = ['Player 1 Wins', 'Player 2 Wins']
values = [player_1_wins, player_2_wins]

plt.bar(labels, values)
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.title(f"Gambler's Ruin Simulation (Simulations: {simulations})")
plt.show()