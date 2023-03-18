import sys
input=sys.stdin.readline

N = int(input())
student = []
for _ in range(N):
    student.append(str(input().rstrip()))

for i in range(1, len(student[0])+1):
    tmp1 = []
    for j in range(N):
        tmp2 = student[j][-i:]
        if tmp2 in tmp1:
            break
        else:
            tmp1.append(tmp2)
    if len(tmp1) == N:
        print(i)
        break