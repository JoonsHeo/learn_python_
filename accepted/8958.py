t = int(input())

cases = []
for i in range(t):
    cases.append(input())

for i in range(t):
    streak = 0
    currentCase = cases[i]
    score = 0

    for j in range(len(currentCase)):
        if currentCase[j] == 'O':
            streak += 1
            score += streak
        else:
            streak = 0
    
    print(score)