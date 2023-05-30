n = int(input())

t_set = set()

for i in range(n):
    t_set.add(input())

m = int(input())
res = 0

for i in range(m):
    if input() in t_set:
        res += 1

print(res)
