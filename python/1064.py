import sys
input=sys.stdin.readline

Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())

if ((Xa-Xb)*(Ya-Yc) == (Ya-Yb)*(Xa-Xc)):
    print(-1.0)


else:
    ab_length = ((Xa-Xb)**2 + (Ya-Yb)**2)**0.5
    ac_length = ((Xa-Xc)**2 + (Ya-Yc)**2)**0.5
    bc_length = ((Xb-Xc)**2 + (Yb-Yc)**2)**0.5

    length = [ab_length + ac_length, ab_length + bc_length, ac_length + bc_length]
    result = max(length) - min(length)
    print(2 * result)