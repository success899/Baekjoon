import sys
input=sys.stdin.readline

N = int(input())

for _ in range(N):
    student = []
    G = int(sys.stdin.readline())
    for _ in range(G):
        student.append(int(input()))
    if G == 1:
        print(1)
    else:
        count = 2
        while 1:
            tmp = []
            for i in range(len(student)):
                tmp.append(student[i] % count)
            set_tmp = list(set(tmp))
            if len(student) == len(set_tmp):
                print(count)
                break
            else:
                count += 1