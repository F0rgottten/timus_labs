# N = 1
# 00 01 (10) 11
# S = 3
# E = 1
# S/E = 3

# N = 2
# 00 01 02 (10) 11 12 (20) (21) 22
# S = 12
# E = 3
# S/E = 4

# N = 3
# 00 01 02 03 11 12 13 22 23 33
# S = 30
# E = 6
# S/E = 5
# Формула - S = N(N + 1)/ 2 * (N + 2) = ((N*(N+1)*(N+2))/2)

n = int(input())
res = ((n * (n + 1) * (n + 2)) // 2)
print(res)
