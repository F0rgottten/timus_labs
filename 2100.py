n = int(input())
res = 200
for i in range(n):
    res += 200 if "+one" in input() else 100
if res == 1300:
    res += 100
print(res)
