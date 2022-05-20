def av_grade(values):
    return sum(values) / len(values)

number_of_students = int(input())
students_grades = {}
for _ in range(number_of_students):
    student, grade = input().split(' ')
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for student, grades in students_grades.items():
    grades_formated = ' '.join(f'{grade:.2f}' for grade in grades)
    average_grade = av_grade(grades)
    print(f"{student} -> {grades_formated} (avg: {average_grade:.2f})")