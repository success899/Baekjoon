n = int(input())
ox_list = []
score = 0
count = 1
score_list=[]
for i in range(0,n):
    ox_list.append(input())

for i in range(0,n):
    for y in range(0,len(ox_list[i])):
        if ox_list[i][y] == "O":
            score += count
            count += 1
        elif ox_list[i][y] == "X":
            count = 1
    score_list.append(score)
    score = 0
    count = 1


for i in range(0,len(score_list)):
    print(score_list[i])