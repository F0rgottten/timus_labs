s = [x for x in input().split()]

n = int(s[0])
k = len(s[1])

n0 = n
k0 = k

# 9 !! = 9 * (9-2) *(9-2*2) * (9-2*3) * (9-2*4)= 945

while n0 - k > 0:
    n *= (n0 - k)
    k += k0

print(n)
