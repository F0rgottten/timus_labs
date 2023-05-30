a, b, c, d = map(int, input().split())

if a >= c:
    print(a)
else:
    while a < c:
        a += b
        if a >= c:
            print(c)
            break
        c -= d
    else:
        print(a)
