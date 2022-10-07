n = int(input())
tmp = 1
x = 1
y = 1
while n > tmp:
    n = n - tmp
    tmp = tmp + 1

if tmp % 2 == 0:
    x = n
    y = tmp - n +1
elif tmp % 2 == 1:
    x = tmp - n +1
    y = n
print(f'{x}/{y}')