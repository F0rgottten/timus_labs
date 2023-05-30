#Высокие затраты по времени
'''n = int(input())
p = [int(input()) for _ in range(n)]

dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    s = 0
    for j in range(i, n):
        s += p[j]
        dp[i] = max(dp[i], s + dp[j + 1])

print(max(dp))'''
# Используем алгоритм Кадане
n = int(input())
p = [0] + [int(input()) for _ in range(n)]
max_sum = 0
max_ending = 0
for i in range(1, n + 1):
    max_ending = max(max_ending + p[i], 0)
    max_sum = max(max_sum, max_ending)
print(max_sum)
