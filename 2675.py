T = int(input())
for _ in range(T):
    R,S = input().split()
    R = int(R)

    for i in S:
        for _ in range(R):
            print(i,end="")
    print("")