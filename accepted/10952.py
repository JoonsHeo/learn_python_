while(1):
    pair = input().split(' ')
    a = int(pair[0])
    b = int(pair[1])
    if a == b == 0:
        break
    print(a + b)