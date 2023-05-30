n = int(input())

for i in range(n - 1):
    print("(", end="")
for i in range(n):
    for j in range(i + 1):
        if j > 0:
            if j % 2 == 0:
                print("+", end="")
            else:
                print("-", end="")
        print(f"sin({j + 1}", end="")

    for j in range(i + 1):
        print(")", end="")
    print(f"+{n-i}", end="")

    if i !=n - 1:
        print(")", end="")