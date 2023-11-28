import sys, math
input=sys.stdin.readline

seq = [1 for _ in range(1000000+1)]
for i in range(1,1000000+1):
    seq[i] = (seq[math.floor(i-math.sqrt(i))] + seq[math.floor(math.log(i))] + seq[math.floor(i*math.sin(i)*math.sin(i))]) % 1000000
    
while True:
    n = int(input())
    if n == -1:
        break
    print(seq[n])