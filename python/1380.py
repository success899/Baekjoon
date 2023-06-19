import sys
input=sys.stdin.readline

result = []

while True:
    n = int(input())
    if n == 0:
        break

    student = []
    for _ in range(n):
        student.append(str(input().rstrip()))

    script = []

    for i in range(2 * n - 1):
        script.append(int(input().split()[0]))
    script.sort()

    for i in range(0, len(script), 2):
        if i == (len(script) - 1) or script[i] != script[i + 1]:
            result.append(student[script[i] - 1])
            break

for i in range(len(result)):
  print(i+1, result[i])