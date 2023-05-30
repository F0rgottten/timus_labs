n = int(input())

group = []

for x in range(n):
    friends = [int(x) for x in input().split() if x != '0']
    group.append(friends)

t1 = set()
t2 = set()

i = 1
t1.add(i)
while i <= n:
    friends = group[i - 1]
    if i in t1:
        for x in friends:
            t2.add(x)
    elif i in t2:
        for x in friends:
            t1.add(x)
    else:
        friends_t1 = False
        for x in friends:
            if x in t1:
                friends_t1 = True
        if friends_t1:
            t2.add(i)
            for x in friends:
                t1.add(x)
        else:
            t1.add(i)
            for x in friends:
                t2.add(x)
    i += 1

print(len(t1))
print(*t1)
