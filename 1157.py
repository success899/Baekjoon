S = input().upper()
S_set = list(set(S))
cnt = []

for i in S_set:
    count = S.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(S_set[(cnt.index(max(cnt)))].upper())