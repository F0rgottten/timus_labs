from math import ceil
k = int(input())
p = [int(x) for x in input().split()]
p.sort()
res = 0
for i in range(len(p) // 2 + 1):
    if p[i] % 2 == 0:
        res += ceil(p[i] / 2) + 1
    else:
        res += ceil(p[i] / 2)
print(res)
