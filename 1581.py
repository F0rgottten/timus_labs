n = int(input())

vas_nums = [int(i) for i in input().split()]
pet_nums = []

count_same = 0
prev = vas_nums[0]

for i in range(n):
    if vas_nums[i] == prev:
        count_same += 1
    else:
        pet_nums.append(count_same)
        pet_nums.append(prev)
        count_same = 1
    if i == n - 1:
        pet_nums.append(count_same)
        pet_nums.append(vas_nums[i])
    prev = vas_nums[i]

print(' '.join(str(x) for x in pet_nums))
