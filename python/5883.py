import sys
input=sys.stdin.readline

B_list = []

for _ in range(int(input())):
    B = input()
    B_list.append(B)

B_set = set(B_list)
result = 1

for i in B_set:
	count = 1
	tmp = -1
	for j in range(len(B_list)):
		if B_list[j] != i:
			if tmp == -1:
				tmp = B_list[j]
			else:
				if tmp == B_list[j]:
					count += 1
				else:
					result = max(result, count) 
					tmp = B_list[j]
					count = 1
	result = max(result, count)
print(result)