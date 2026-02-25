nums = []

for i in range(9):
    nums.append(input())

for i in range(9):
    nums[i] = int(nums[i])

highNum = 0
highIdx = 0

for i in range(9):
    if nums[i] > highNum:
        highNum = nums[i]
        highIdx = i

print(highNum)
print(highIdx + 1)