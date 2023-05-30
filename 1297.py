s = input()
n = len(s)

d = [[0] * n for _ in range(2)]
for p in range(2):
    l, r = 0, -1
    for i in range(n):
        k = (0 if i > r else min(d[p][l + r - i] - p, r - i)) + 1
        try:
            while i + k - 1 < n and i - k + p >= 0 and s[i + k - 1] == s[i - k + p]:
                k += 1
        except IndexError:
            pass
        k -= 1
        d[p][i] = k
        if i + k > r:
            l, r = i - k + p, i + k - 1

m1 = 0
m2 = 0
for i in range(1, n):
    if d[1][m1] < d[1][i]:
        m1 = i
    if d[0][m2] < d[0][i]:
        m2 = i

if d[1][m1] > d[0][m2]:
    print(s[m1 - d[1][m1] + 1:m1 + d[1][m1]])
else:
    print(s[m2 - d[0][m2]:m2 + d[0][m2]])
