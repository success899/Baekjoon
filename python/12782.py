import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N, M = map(str, input().split())
    zero, one = 0, 0

    for i in range(len(N)):
        if N[i] != M[i]:
            if M[i] == '1':
                one += 1
            else:
                zero += 1
                
    print(max(one, zero))