import sys, math
input=sys.stdin.readline

for _ in range(int(input())):
    num_list = list(map(int, input().split()))
    result = []

    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            tmp = math.gcd(num_list[i], num_list[j])
            result.append(tmp)
    
    print(max(result))