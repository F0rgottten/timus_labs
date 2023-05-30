A, B, C = map(int, input().split())

if C > A + B:
    print("Impossible")
elif C <= max(A, B):
    if A >= C > B :
        first = C
        second = 0
    else:
        first = 0
        second = C
    print(first, second)
else:
    x = C - B
    y = B
    if x > A:
        x = A
        y = C - x
    print(x, y)