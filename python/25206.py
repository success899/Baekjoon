import sys, math
input=sys.stdin.readline

sum_grade = 0
count = 0

for _ in range(20):
    subject, grade, ranking = map(str, input().split())
    grade = float(grade)
    if ranking != 'P':
        count += grade
        if ranking == 'A+':
            sum_grade += (4.5*grade)
        elif ranking == 'A0':
            sum_grade += (4.0*grade)
        elif ranking == 'B+':
            sum_grade += (3.5*grade)
        elif ranking == 'B0':
            sum_grade += (3.0*grade)
        elif ranking == 'C+':
            sum_grade += (2.5*grade)
        elif ranking == 'C0':
            sum_grade += (2.0*grade)
        elif ranking == 'D+':
            sum_grade += (1.5*grade)
        elif ranking == 'D0':
            sum_grade += (1.0*grade)

print(round(sum_grade/count,6))