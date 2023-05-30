A = int(input())
B = int(input())
res = 0
for i in range(A, B+1):
    if i % 2 == 1:
        res += 1
print(res)
