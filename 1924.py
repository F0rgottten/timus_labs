# 1 + 2 - 3 + 4 - 5 + 6 - 7... n
n = int(input())
res = 1
i = 1
while i < n:
    if i % 2 != 0:
        res += i + 1
    else:
        res -= i + 1
    i += 1

if res % 2 == 0:
    print('black')
else:
    print('grimy')
