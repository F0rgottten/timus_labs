# 4 1 6 5 3 4 3
# 7 6 6 4 2 1
# 6 5 4 4 3 3 1
n = int(input())
res = [int(input()) for _ in range(n)]
res = (sorted(res, reverse=True))
for x in res:
    print(x)
