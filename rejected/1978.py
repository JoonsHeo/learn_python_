n = int(input())

# make a matrix from 1 to 1000

nums = input().split(" ")

for i in range(n):
    nums[i] = int(nums[i])

isPrime = []
for i in range(1001):
    isPrime.append(1)

for i in range(2, 1001):
    if not isPrime[i]:
        break
    for j in range(1001):
        if i*j > 1000:
            break
        isPrime[i*j] = 0
        
cnt = 0
for i in range(n):
    if isPrime[nums[i]] == 1:
        cnt += 1

print(cnt)