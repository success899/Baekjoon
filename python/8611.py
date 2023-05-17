import sys
input=sys.stdin.readline

n = int(input())
tmp = True

for i in range(2,11):
  m = n
  result = ""

  while m > 0:
    result = str(m % i) + result
    m = m // i

  if result == result[::-1]:
    print(i, end=' ')
    print(result)
    tmp = False

if tmp == True:
  print("NIE")