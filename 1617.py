n = int(input())
d = []

for i in range(n):
    d.append(int(input()))

wheels = {i: d.count(i) for i in d if d.count(i) >= 4}
res = 0

for x in wheels:
    res += wheels[x] // 4

print(res)
