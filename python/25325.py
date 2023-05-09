import sys
input=sys.stdin.readline

N = int(input())
student = map(str, input().rstrip().split())
result = dict.fromkeys(student, 0)

for _ in range(N) :
    tmp = map(str, input().rstrip().split())
    for i in tmp:
        result[i] += 1

sort_dict = sorted(result.items(), key=lambda x: x[1], reverse=True)

for key, value in sort_dict:
    print(key, value)