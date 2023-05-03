list_1 = ['a','i','y','e','o','u']
list_2 = ['b','k','x','z','n','h','d','c','w','g','p','v','j','q','t','s','r','l','m','f']

while True:
    try:
        S = input()
        result = ""
        for i in range(len(S)):
            if S[i].lower() in list_1:
                if S[i].isupper():
                    tmp = S[i].lower()
                    for j in range(6):
                        if list_1[j] == tmp:
                            a = list_1[(j+3)%6]
                            result += a.upper()
                elif S[i].islower():
                    for j in range(6):
                        if list_1[j] == S[i]:
                            a = list_1[(j+3)%6]
                            result += a

            elif S[i].lower() in list_2:
                if S[i].isupper():
                    tmp = S[i].lower()
                    for j in range(20):
                        if list_2[j] == tmp:
                            a = list_2[(j+10)%20]
                            result += a.upper()
                elif S[i].islower():
                    for j in range(20):
                        if list_2[j] == S[i]:
                            a = list_2[(j+10)%20]
                            result += a
            else:
                result += S[i]

        print(result)

    except:
        break