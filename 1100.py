n = int(input())

nums = {str(x) : [] for x in range(100, -1, -1)}
for x in range(n):
    ID, m = input().split()
    nums[m].append(ID)

for k, v in nums.items():
    if len(v) != 0:
        for i in range(len(v)):
            print(v[i], k)