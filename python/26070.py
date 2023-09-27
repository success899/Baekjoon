A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())
result = 0

for _ in range(3):

    chicken = min(A, X)
    result += chicken
    A -= chicken
    X -= chicken

    pizza = min(B, Y)
    result += pizza
    B -= pizza
    Y -= pizza

    burger = min(C, Z)
    result += burger
    C -= burger
    Z -= burger

    Y, Z, X = X // 3, Y // 3, Z // 3

print(result)