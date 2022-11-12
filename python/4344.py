C = int(input())
N = []
student_count = 0
student_sum = 0
student_sum_list = []
student_mean = []
student_count_list = []
student_ratio = []
student_sp = 0
for i in range(0,C):
    student_score = input().split()
    N.append(student_score)

for i in range(0,len(N)):
    for y in range(1,int(N[i][0])+1):
        student_sum += int(N[i][y])
    student_sum_list.append(student_sum)
    student_sum = 0

for i in range(0,len(student_sum_list)):
    student_mean.append(float(student_sum_list[i]/int(N[i][0])))

for i in range(0,len(student_mean)):
    for y in range(1,int(N[i][0])+1):
        if student_mean[i] < int(N[i][y]):
            student_count += 1
    student_count_list.append(student_count)
    student_count = 0

for i in range(0,len(student_count_list)):
    student_sp = student_count_list[i]/int(N[i][0])*100
    student_ratio.append(round(student_sp,3))

for i in range(0,len(student_ratio)):
    print("{:.3f}%".format(student_ratio[i]))