N = int(input())

member_list = []

for i in range(N):
    age, name = map(str,input().split())
    member_list.append([int(age), i, name])

member_list.sort()

for i in range(N):
    print(member_list[i][0], member_list[i][2])