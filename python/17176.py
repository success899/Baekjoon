import sys
input=sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
text = list(str(input().rstrip()))
pw = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

if len(N_list) == len(text):
    tmp = []

    for i in N_list:
        tmp.append(pw[i])

    tmp.sort()
    text.sort()

    for i in range(N):
        if tmp[i] != text[i]:
            print('n')
            break
    else:
        print('y')

else:
    print('n')