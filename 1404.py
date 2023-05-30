word = input()
nums = []
for letter in word:
    num = ord(letter) - ord('a')
    nums.append(num)
for i in range(1, len(nums)):
    nums[i] -= sum(nums[:i])
nums[0] = nums[0] - 5 if nums[0] - 5 >= 0 else 26 - nums[0] - 5
for i in range(1, len(nums)):
    nums[i] %= 26
result = ''
for num in nums:
    letter = chr(num + ord('a'))
    result += letter

print(result)
