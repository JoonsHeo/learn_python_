from math import ceil, floor

n = int(input())

sizes = input().split(' ')
for i in range(6):
    sizes[i] = int(sizes[i])

tp = input().split(' ')
t = int(tp[0])
p = int(tp[1])

tees = 0
for i in range(6):
    tees += ceil(sizes[i] / t)

penBoxes = 0
pens = 0
penBoxes = floor(n / p)
pens = n % p

print(f"{tees}\n{penBoxes} {pens}")