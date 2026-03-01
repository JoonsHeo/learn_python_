n = int(input())

nums = input().split(' ')
for i in range(n):
    nums[i] = int(nums[i])

maxVal = nums[0]
maxIdx = 0
for i in range(1, n):
    if nums[i] > maxVal:
        maxVal = nums[i]
        maxIdx = i

avg = 0
for i in range(n):
    avg += nums[i]
avg = avg / n / maxVal * 100

print(avg)