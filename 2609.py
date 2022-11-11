import sys, math
input = sys.stdin.readline

N_list = list(map(int,input().split()))

gcd = math.gcd(N_list[0],N_list[1])
print(gcd)
print(int(N_list[0]*N_list[1]/gcd))

# 시간 초과
# #최대 공약수
# for i in range(min(N_list[0],N_list[1]),0,-1):
#     if N_list[0]%i ==0 and N_list[1]%i==0:
#         print(i)
#         break

# #최소 공배수
# for i in range(max(N_list[0],N_list[1]),(N_list[0]*N_list[1])+1):
#     if i%N_list[0]==0 and i%N_list[1]==0:
#         print(i)
#         break
