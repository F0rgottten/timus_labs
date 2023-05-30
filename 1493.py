n = int(input())

next_t = list(int(x) for x in str(n + 1).zfill(6))
prev_t = list(int(x) for x in str(n - 1).zfill(6))

print("Yes" if sum(next_t[:3]) == sum(next_t[3:]) or sum(prev_t[:3]) == sum(prev_t[3:]) else "No")