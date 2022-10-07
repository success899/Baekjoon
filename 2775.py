t = int(input())

for i in range(t):

    k = int(input())
    n = int(input())
    hm_cnt = [ho for ho in range(1,n+1)]

    for x in range(k):
        for y in range(1,n):
            hm_cnt[y] += hm_cnt[y-1]
    print(hm_cnt[-1])