import math

n = int(input())

for i in range(n):
    k = int(input())
    k -= 1  # т.к. позиция задается с единицы

    t = k * 8 + 1
    if int(math.sqrt(t)) ** 2 == t:
        print('1 ', end='')
    else:
        print('0 ', end='')

# 1 10 100 1000 10000 100000 1000000...
# 0 1 3 6 10 15 21 ...

# 8 * 0 + 1 = 1
# 8 * 1 + 1 = 9
# 8 * 2 + 1 = 25
# 8 * 3 + 1 = 49
