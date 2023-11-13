import sys, collections
input=sys.stdin.readline

S = input().rstrip()
dq = collections.deque()

for i in range(len(S)):
    try:
        dq.append(int(S[i]))
        
    except:
        if S[i] == '+':
            result = (dq.pop() + dq.pop())

        elif S[i] == '-':
            tmp1 = dq.pop()
            tmp2 = dq.pop()
            result = tmp2 - tmp1

        elif S[i] == '*':
            result = (dq.pop() * dq.pop())

        elif S[i] == '/':
            tmp1 = dq.pop()
            tmp2 = dq.pop()
            result = tmp2 // tmp1

        dq.append(result)

print(dq.pop())