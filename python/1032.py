import sys
input=sys.stdin.readline

N = int(input())
cmd_str = list(input().rstrip())

for _ in range(N-1):
    cmd_tmp = list(input().rstrip())
    for j in range(len(cmd_str)):
        if cmd_str[j] != cmd_tmp[j]:
            cmd_str[j] = '?'
print(''.join(cmd_str))