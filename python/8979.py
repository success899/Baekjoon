import sys
input=sys.stdin.readline

N, K = map(int,input().split())

score = [[] for _ in range(N+1)]
count = 1

for _ in range(N):
    country, gold, silver, bronze = map(int, sys.stdin.readline().split())
    score[country] = [gold, silver, bronze]

gold_K, silver_K, bronze_K = score[K]

for i in range(1, N+1):
    if gold_K < score[i][0]:
        count += 1
    elif gold_K == score[i][0]:
        if silver_K < score[i][1]:
            count += 1
        elif silver_K == score[i][1]:
            if bronze_K < score[i][2]:
                count += 1
                
print(count)