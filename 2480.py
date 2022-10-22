A, B, C = list(map(int,input().split()))


if A == B == C:
    goal = 10000+A*1000
elif A == B:
    goal = 1000+A*100
elif A == C:
    goal = 1000+A*100
elif B == C:
    goal = 1000+B*100
else:
    goal = max(A,B,C)*100

print(goal)