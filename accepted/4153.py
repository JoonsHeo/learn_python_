while(1):
    oneLine = input().split(" ")
    a = int(oneLine[0])
    b = int(oneLine[1])
    c = int(oneLine[2])

    if a == b == c == 0:
        break

    max = a
    if b > max:
        max = b
    if c > max:
        max = c

    if (max**2)*2 - a**2 - b**2 - c**2 == 0:
        print("right")
    else:
        print("wrong")