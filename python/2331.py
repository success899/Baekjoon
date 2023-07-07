import sys
input=sys.stdin.readline

D, P = map(int, input().split())
num_list = [D]

while True:
    tmp = 0
    for i in str(num_list[-1]):
        tmp += int(i) ** P
        
    if tmp in num_list:
        break

    num_list.append(tmp)

print(num_list.index(tmp))