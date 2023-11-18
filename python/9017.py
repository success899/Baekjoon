import sys
input=sys.stdin.readline

for i in range(int(input())):
	N = int(input())
	T_list = list(map(int, input().strip().split()))

	manage = dict()
	
	for j in range(N):
		if T_list[j] not in manage:
			manage[T_list[j]] = [1, [], 0]
		else:
			manage[T_list[j]][0] += 1

	contain = set(k for k, v in manage.items() if v[0] < 6)

	grade = 1
	for j in range(N):
		if T_list[j] not in contain:
			manage[T_list[j]][1].append(grade)
			if len(manage[T_list[j]][1]) <= 4: 
				manage[T_list[j]][2] += grade
			grade += 1

	result = []
	
	for k, v in manage.items():
		if len(v[1]) != 0 and v[2] != 0:
			result.append([k, v[1][4], v[2]])

	a = sorted(result, key = lambda x : (x[2], x[1]))
	print(a[0][0])