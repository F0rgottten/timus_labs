n = int(input())
studList = [input() for _ in range(n*2)]
students = {"Slytherin":[],"Hufflepuff":[],"Gryffindor":[],"Ravenclaw":[]}
for i in range(1, n*2+1, 2):
    students[studList[i]] = students.get(studList[i],[]) + [studList[i-1]]
for key, value in students.items():
    print(key + ":")
    for i in range(len(students[key])):
        print(value[i])
    print()