import numpy as np
import matplotlib.pyplot as plt
import math

# 目標: 證明 P(up A before down B) = B / (A + B)

# ∆t
delta_t = 0.01

# 常態分配 X 的參數
mu = 0               # 平均
sigma = 1 * math.sqrt(delta_t)  # 標準差
num_samples = 1      # 樣本數

# 模擬次數
times = 1000

succ_times = 0
fail_times = 0

# A, B
A = 1
B = 2 

start = 0
num = start 

for _ in range(times): 

    num = start 

    while num > (start - B) and num < (start + A):
    
        # X ~ N(0, 1 * ∆t)
        X = np.random.normal(mu, sigma, num_samples)

        num += X

    if num >= (start + A):
        succ_times += 1
    else:
        fail_times += 1

print("Start with", start)
print("end with", A, "for", succ_times, "times")
print("end with", -B, "for", fail_times, "times")
print("P(up A(",A,") before down B(",B,")) =", succ_times / times)


