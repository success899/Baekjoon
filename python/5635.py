import sys
input=sys.stdin.readline

n = int(input())

student = []

for _ in range(n):
    name, day, month, year = input().rstrip().split()
    day, month, year = map(int,(day, month, year))
    student.append((year, month, day, name))

student.sort()
print(f'{student[-1][3]}\n{student[0][3]}')