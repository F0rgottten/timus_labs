n = int(input())
monitor = [[0 for x in range(n)] for y in range(n)]

row = 0
for line in range(n):
    current_line = input().split()
    column = 0
    for number in current_line:
        monitor[row][column] = int(number)
        column += 1
    row += 1

row = 0
while row < len(monitor):
    column = 0
    depth = row
    while depth >= 0:
        print(monitor[depth][column], end=" ")
        depth -= 1
        column += 1
    row += 1

column = 1
while column < len(monitor):
    row = len(monitor) - 1
    depth = column
    while depth < len(monitor):
        print(monitor[row][depth], end=" ")
        row -= 1
        depth += 1
    column += 1