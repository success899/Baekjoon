import sys
input=sys.stdin.readline

switch_num = int(input())
switch_status = list(map(int, input().split()))
student_count = int(input())
student_status = []
for i in range(student_count):
    student_status.append(list(map(int, input().split())))

for i in student_status:

    if i[0] == 1:
        for j in range(len(switch_status)):
            if (j + 1) % i[1] == 0:
                switch_status[j] = int(not switch_status[j])

    else:
        for j in range(len(switch_status)):
            if (j + 1) == i[1]:
                plus = j + 1
                minus = j - 1
                switch_status[j] = int(not switch_status[j])
                while True:
                    if minus >= 0 and plus < len(switch_status):
                        if switch_status[minus] == switch_status[plus]:
                            switch_status[minus] = int(not switch_status[minus])
                            switch_status[plus] = int(not switch_status[plus])
                        else:
                            break
                    else:
                        break

                    minus -= 1
                    plus += 1

count = 0
while count < len(switch_status):

    print(switch_status[count], end=" ")
    if count % 20 == 19:
        print()
    count += 1