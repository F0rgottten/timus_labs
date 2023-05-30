import random

n = int(input())
d = [int(i) for i in input().split()]
random.shuffle(d)
res = 0
mass = sum(d)
for i in d:
    res += mass * i
    mass -= i
    res += mass * i
print(res)
