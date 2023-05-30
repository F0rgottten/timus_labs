N, M, Y = map(int, input().split())
exists = False
for x in range(M):
    if x ** N % M == Y:
        print(x, end=' ')
        exists = True
print("" if exists else -1)
