nums = input().split(' ')

check = 0
for i in range(5):
    check += int(nums[i])^2

print(check//10)