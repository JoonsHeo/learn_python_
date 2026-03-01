num = 1
while(num != 0):
    num = input()
    length = len(num)
    isPalin = True
    for frontIdx in range(length // 2):
        backIdx = length - 1 - frontIdx
        if num[frontIdx] != num[backIdx]:
            isPalin = False
    if isPalin:
        print("yes")
    else:
        print("no")