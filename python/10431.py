import sys
input=sys.stdin.readline

for _ in range(int(input())):
    student = list(map(int, input().split()))
    result = 0
    for i in range(1,len(student)-1):
        for j in range(i+1,len(student)):
            if student[i] > student[j]:
                student[i], student[j] = student[j], student[i]
                result += 1
    print(student[0], result)