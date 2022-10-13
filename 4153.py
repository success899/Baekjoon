a =[]
while True:
    a = list(map(int,input().split()))
    b = max(a)
    a.remove(b)

    if a[0] == 0 and a[1] == 0 and b == 0:
        break
    elif (a[0]**2 + a[1] **2) == b**2 :
        print("right")
    else:
        print("wrong")
    a.clear
