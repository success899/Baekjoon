import collections

while True:
    try:
        a = input()
        b = input()
        alpha1 = collections.defaultdict(int)
        alpha2 = collections.defaultdict(int)
        result = ''
        for s in a:
            alpha1[s] += 1
        for s in b:
            alpha2[s] += 1
        s = []
        for char in alpha1:
            if char in alpha2:
                s.append(char)
        s.sort()
        for char in s:
            result += char*min(alpha1[char], alpha2[char])
        print(result)
    except:
        break