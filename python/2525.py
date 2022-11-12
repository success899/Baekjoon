A, B = list(map(int,input().split()))
C = int(input())
temp = B+C

while(1):
    if temp >= 60:
        A+=1
        temp-=60
        if A == 24:
            A = 0
    elif temp < 60:
        break

print(A, temp)