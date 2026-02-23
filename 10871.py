n, x = input().split()

n = int(n)
x = int(x)

nums = input().split()

for i in range(n):
    nums[i] = int(nums[i])
    if(nums[i] < x):
        print(f"{nums[i]} ", end='')
