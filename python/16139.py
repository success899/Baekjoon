import sys
input=sys.stdin.readline

S = input().strip()
Q = int(input())

# 50점
for _ in range(Q):
    find_list = input().split()
    find_list[1] = int(find_list[1])
    find_list[2] = int(find_list[2])+1
    print(S[find_list[1]:find_list[2]].count(find_list[0]))


# 100점
S_temp = [[0]*26]
S_temp[0][ord(S[0]) - 97] = 1
for i in range(1, len(S)):
    S_temp.append(S_temp[-1][:])
    S_temp[i][ord(S[i])-97] += 1
for i in range(Q):
    c,start,end = list(input().split())
    start,end = int(start), int(end)
    if start == 0:
        print(S_temp[end][ord(c)-97])
    else:
        print(S_temp[end][ord(c)-97]-S_temp[start-1][ord(c)-97])