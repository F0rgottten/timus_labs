n = int(input())
grades = []
for i in range(n):
    grades.append(int(input()))
if 3 in grades:
    print("None")
elif sum(grades) == 5 * n:
    print("Named")
elif sum(grades) / n >= 4.5:
    print("High")
else:
    print("Common")
