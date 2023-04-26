import sys
input=sys.stdin.readline

keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./"

while True:

    text = str(input()).rstrip()
    result = ''

    if text == '':
        break

    for i in range(len(text)):
        if text[i] != ' ':
            result += keyboard[keyboard.index(text[i]) - 1]
        else:
            result += ' '

    print(result)