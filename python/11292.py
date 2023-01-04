import sys
input=sys.stdin.readline

while True:
    N = int(input())

    if N == 0:
        break

    student, result = [], []
    tmp = 0

    for _ in range(N):
        name, height = input().split()
        height = float(height)
        student.append([name, height])
    
    student.sort(key = lambda x:-x[1])

    for name, height in student:
        if height >= tmp:
            result.append(name)
            tmp = height
        
    for i in result:
        print(i,end=' ')
    print()