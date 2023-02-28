import sys
input=sys.stdin.readline

N, M, K = map(int,input().split())

score = {}

for idx in range(M):
    tmp = list(map(float, input().split()))
    if idx == 0:
        for j in range(0,len(tmp),2):
            score[tmp[j]] = tmp[j+1]
    else:
        for j in range(0,len(tmp),2):
            if score[tmp[j]] < tmp[j+1]:
                score[tmp[j]] = tmp[j+1]

score = sorted(list(score.values()), reverse=True)
result = sum(score[:K])
print(f'{result:.1f}')