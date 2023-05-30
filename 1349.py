
n = int(input())
min_a, min_b, min_c = 101, 101, 101
found_solution = False

for a in range(1, 101):
    for b in range(1, 101):
        for c in range(1, 101):
            if a ** n + b ** n == c ** n:
                found_solution = True
                if a < min_a or (a == min_a and b < min_b) or (a == min_a and b == min_b and c < min_c):
                    min_a, min_b, min_c = a, b, c

if found_solution:
    print(min_a, min_b, min_c)
else:
    print(-1)
