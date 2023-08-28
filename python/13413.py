import sys
input=sys.stdin.readline

results = []
result = 0
arr = []

for _ in range(int(input())):
    N = int(input().rstrip())
    start = list(input().rstrip())
    target = list(input().rstrip())

    for i in range(N):
        if start[i] != target[i]:
            arr.append(start[i])

    if arr.count("B") >= arr.count("W"):
        result = arr.count("B")
    else:
        result = arr.count("W")
    results.append(result)
    arr = []

for answer in results:
    print(answer)