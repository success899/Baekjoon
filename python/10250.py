for i in range(int(input())):
    h,w,n = map(int,input().split())

    xx = n//h+1
    xxx = n%h
    
    if n % h == 0:
        xx = n // h
        xxx = h

    print(f'{xxx*100+xx}')