n = input()
hansu_cnt = 0

for i in range(1,int(n)+1):
    if i <= 99:
        hansu_cnt += 1
    elif i <= 999:
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
            hansu_cnt += 1

print(hansu_cnt)