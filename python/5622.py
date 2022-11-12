dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
n = input()
time_cnt = 0
for j in range(len(n)):
    for i in dial:
        if n[j] in i:
            time_cnt += dial.index(i)+3
print(time_cnt)