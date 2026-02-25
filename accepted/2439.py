N = int(input())

for i in range(N):
    out = ''
    stars = i + 1
    spaces = N - stars
    out += ' ' * spaces
    out += '*' * stars
    print(out)