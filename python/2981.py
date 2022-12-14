import sys
from math import gcd
input=sys.stdin.readline

N = int(input())
M_list = []
tmp_list = []

for _ in range(N):
    M_list.append(int(input()))

for i in range(N):
    tmp_list.append(abs(M_list[i] - M_list[i-1]))
tmp_list = list(set(tmp_list))
tmp_list.sort()

if len(tmp_list) != 1:
    tmp = gcd(tmp_list[0],tmp_list[1])
else:
    tmp = tmp_list[0]
result = []

for i in range(2,int(tmp**0.5)+1):
    if tmp % i == 0:
        result.append(i)
        if i != tmp//i:
            result.append(tmp//i)

result.append(tmp)
result.sort()
for i in result:
    print(i,end=' ')