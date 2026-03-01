# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

# which sorting algorithm to use? -> merge?

# def mergesort(bigList):
#     l = len(biglist)
#     if l == 1:
#         return bigList
#     elif l == 2: # is this case really necessary?
#         if bigList[0] > bigList[1]:
#             temp = bigList[0]
#             bigList[0] = bigList[1]
#             bigList[1] = temp
#         return bigList
#     else:
#         # merge two lists and create a new one

# WIP
        
# find nth lowest sort

for i in range(n):

    for j in range(i+1, n):
        if nums[j] < nums[i]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

    print(nums[i])

# 메모리 초과