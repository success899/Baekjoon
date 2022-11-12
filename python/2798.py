n , m = map(int,input().split())
card_list = list(map(int,input().split()))
tmp_list = []

for i in range(0,n-2):
    for x in range(i+1,n-1):
        for y in range(x+1,n):
            if card_list[i]+card_list[x]+card_list[y] <= m:
                tmp_list.append(card_list[i]+card_list[x]+card_list[y])

       
print(max(tmp_list))