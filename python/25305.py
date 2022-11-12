N, K = list(map(int,input().split()))
score_list = list(map(int,input().split()))

score_list.sort(reverse=True)
print(score_list[K-1])