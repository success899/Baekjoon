n = input()
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cro:
    n = n.replace(i,'#')
print(len(n))