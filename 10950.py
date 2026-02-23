T = int(input())

numPairs = []

for i in range(T):
    numPairs.append(input())

for i in range(T):
    splitNums = numPairs[i].split(' ')
    splitNums[0] = int(splitNums[0])
    splitNums[1] = int(splitNums[1])

    print(splitNums[0] + splitNums[1])