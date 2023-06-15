import sys
input=sys.stdin.readline

meter = int(input())
length = len(str(meter))
result = 0

for i in range(length):
    num = meter % 10
    meter = meter // 10

    if num >4:
        result += (num-1) * (9**i)
    else:
        result += num * (9**i)
print(result)