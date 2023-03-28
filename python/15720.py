import sys
input=sys.stdin.readline

B, C, D = map(int, input().split())
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))
D_list = list(map(int, input().split()))
B_list.sort(reverse=True)
C_list.sort(reverse=True)
D_list.sort(reverse=True)

result = 0
min_list = min(B, C, D)

for i in range(min_list):
    result += (B_list[i] + C_list[i] + D_list[i]) * 0.9

result += sum(B_list[min_list:])
result += sum(C_list[min_list:])
result += sum(D_list[min_list:])

print(sum(B_list) + sum(C_list) + sum(D_list))
print(int(result))