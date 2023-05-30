N = int(input())
nuts = []
hunger = []
hungry = 2
satisfied = 10
for i in range(N):
    value, state = input().split()
    nuts.append(int(value))
    hunger.append(state)
for n, h in zip(nuts, hunger):
    if h == "hungry" and n > hungry:
        hungry = n
    elif h == "satisfied" and n < satisfied:
        satisfied = n
if hungry >= satisfied:
    print("Inconsistent")
else:
    print(satisfied)