n = int(input())
solList = [input() for _ in range(n)]
solSet = set(solList)
for sol in solSet:
    if solList.count(sol) > 1:
        print(sol)