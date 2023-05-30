n = int(input())
variants = ["16", "06", "68", "88"]
# 10 11 16 18 19 60 61 66 68 69 80 81 86 88 89 90 91 96 98 99
if n > 4:
    print("Glupenky Pierre")
else:
    res = []
    for i in range(n):
        res.append(variants[i])
    print(" ".join(res))
