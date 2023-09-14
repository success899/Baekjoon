# import sys
# input=sys.stdin.readline
from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

cryptogram = input()
N_list = []

for i in range(int(input())):
    N_list.append(input())

printed = False

for i in N_list:
    if i in cryptogram:
        print(cryptogram)
        printed = True
        break

if not printed:
    for i in range(1, 26):
        alpha = {}
        for j in range(26):
            a = j+i
            if a > 25:
                a -= 26
            alpha[alphabet_list[j]] = alphabet_list[a]
        decode = ""

        for j in cryptogram:
            decode += alpha[j]
            
        for j in N_list:
            if j in decode:
                print(decode)
                break