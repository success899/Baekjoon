import sys
input=sys.stdin.readline

def check(i):
	tmp = 0
	for j in range(N):
		if j < i:
			if n_list[j] != (n_list[i] - (i-j) * K):
				tmp += 1
		elif j > i:
			if n_list[j] != (n_list[i] + (j-i) * K):
				tmp += 1
	return tmp

N, K = map(int,input().split())
n_list = list(map(int,input().split()))
min_count = 1001

for i in range(N):
	if n_list[i] > i * K:
		count = check(i)
		min_count = min(min_count, count)

print(min_count)