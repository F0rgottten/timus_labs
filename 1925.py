N, K = map(int, input().split())
bomb_alien = []
bomb_human = []
for i in range(N):
    bg = [int(x) for x in input().split()]
    bomb_alien.append(bg[0])
    bomb_human.append(bg[1])
B = 0
G = 0
for b, g in zip(bomb_alien, bomb_human):
    B += b
    G += g
res = B + K - G - N * 2 - 2
print(res if res > 0 else "Big Bang!")
