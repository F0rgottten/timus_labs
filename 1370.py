nm = [x for x in input().split()]
N = int(nm[0])
M = int(nm[1]) % N
nums = []
res_nums = []
for i in range(N):
    nums.append(input())
for j in range(10):
    t = j + M if j + M < N else j + M - N
    res_nums.append(nums[t])

print(''.join(x for x in res_nums))
