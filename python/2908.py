n = input().split()

n_1 = ""
n_2 = ""
for i in range(len(n[0])-1,-1,-1):
    n_1 += n[0][i]

for i in range(len(n[1])-1,-1,-1):
    n_2 += n[1][i]

if int(n_1) > int(n_2):
    print(n_1)
else:
    print(n_2)
