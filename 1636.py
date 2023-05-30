T1, T2 = map(int, input().split())
attempts = [int(i) for i in input().split()]
for attempt in attempts:
    T1 += attempt * 20
print("No chance." if T1 <= T2  else "Dirty debug :(")
