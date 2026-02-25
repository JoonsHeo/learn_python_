nums = []

for i in range(10):
    nums.append(int(input())%42)

remainders = []
for i in range(42):
    remainders.append(0)

for i in range(10):
    remainders[nums[i]] = 1

cnt = 0
for i in range(42):
    cnt += remainders[i]

print(cnt)