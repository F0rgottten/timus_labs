nk = [x for x in input().split()]
n = int(nk[0])
k = int(nk[1])
droids = [k] * n
gungans = [int(i) for i in input().split()]
# d d d d d// d d d d d// d d d d d// d d d d d
# b b // b b b b b b b// b b b b b // -
unused = 0
survivors = 0

for i in range(len(gungans)):
    unused += gungans[i] - droids[i] if gungans[i] - droids[i] > 0 else 0
    survivors += droids[i] - gungans[i] if droids[i] - gungans[i] > 0 else 0

print(unused, survivors)
