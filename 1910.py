n = int(input())
wall = [int(i) for i in input().split()]
maxPower = 0
index = 0
for brick in range(1, len(wall) - 1):
    power = wall[brick] + wall[brick + 1] + wall[brick - 1]
    if power > maxPower:
        maxPower = power
        index = brick + 1

print(maxPower, index)
