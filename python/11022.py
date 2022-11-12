T = input()
T = int(T)

for i in range(0,T):
    A,B = input().split()
    A = int(A)
    B = int(B)

    print(f'Case #{i+1}: {A} + {B} = {A+B}')