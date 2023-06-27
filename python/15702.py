import sys
input=sys.stdin.readline

N, M = map(int, input().split())
score = list(map(int, input().split()))
student = []
score_board = [0] * M

for i in range(M):
    student.append(list(map(str, input().split())))
    student[i][0] = int(student[i][0])
student.sort(key=lambda x:x[-0])

for i in range(M):
    for j in range(N):
        if student[i][j+1] == 'O':
            score_board[i] += score[j]
max_score = max(score_board)

for i in range(M):
    if max_score == score_board[i]:
        print(f'{student[i][0]} {max_score}')
        break