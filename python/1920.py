N = int(input())
N_list = list(map(int,input().split()))
N_list.sort()
M = int(input())
M_list = list(map(int,input().split()))

for i in M_list:
    start = 0
    end = N-1
    result = 0
    while (start <= end):
        mid = (start+end) //2
        if N_list[mid] == i:
            result = 1
            break
        elif i < N_list[mid]:
            end = mid-1
        else:
            start = mid+1
    print(result)