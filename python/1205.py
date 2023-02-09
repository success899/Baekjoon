import sys
input=sys.stdin.readline

N, score, P = map(int, input().split())

if N == 0:
    print(1)

else:
    score_list = list(map(int, input().split()))
    score_list.append(score)
    score_list.sort(reverse=True)
    index = score_list.index(score) + 1

    if index > P or (N == P and score == score_list[-1]):
        print(-1)
    else:
        print(index)