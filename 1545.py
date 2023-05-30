N = int(input())
eiList = [input() for _ in range(N)]
symbol = input()

for ei in eiList:
    if ei[:len(symbol)] == symbol:
        print(ei)
