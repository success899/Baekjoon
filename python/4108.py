import sys
input=sys.stdin.readline

while True:
    R, C = map(int, input().split())

    if R == 0 and C == 0:
        break

    else:
        mine_map = []
        result = [[0 for j in range(C)] for i in range(R)]
        for _ in range(R):
            mine_map.append(list(str(input().rstrip())))

        for i in range(R):
            for j in range(C):
                if mine_map[i][j] in '*':
                    result[i][j] = '*'
                    if j-1 >= 0 and result[i][j-1] != '*':
                        result[i][j-1] += 1
                    if i-1 >= 0 and result[i-1][j] != '*':
                        result[i-1][j] += 1
                    if i+1 < R and j-1 >= 0 and result[i+1][j-1] != '*':   
                        result[i+1][j-1] += 1
                    if j+1 < C and i-1 >= 0 and result[i-1][j+1] != '*':
                        result[i-1][j+1] += 1
                    if i-1 >= 0 and j-1 >= 0 and result[i-1][j-1] != '*':
                        result[i-1][j-1] += 1
                    if i+1 < R and result[i+1][j] != '*':
                        result[i+1][j] += 1
                    if j+1 < C and result[i][j+1] != '*':
                        result[i][j+1] += 1
                    if j+1 < C and i+1 < R and result[i+1][j+1] != '*':
                        result[i+1][j+1] += 1


        for i in range(R):
            print(*result[i], sep="")