n = int(input())
l = 0
step = 1 if n > 0 else -1
n = n + 1 if n > 0 else n - 1
sum = 0
for i in range(1, n, step):
    sum += i

print(sum)
