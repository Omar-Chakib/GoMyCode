import numpy as np

# Function to calculate grades based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B+'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'F'

number_students = int(input("input the number of students: "))
number_subjects = int(input("input the number of subjects: "))

grades = []

for student in range(number_students):
    print(f"Enter grades for student {student + 1}:")
    student_grades = []
    for subject in range(number_subjects):
        mark = float(input(f"Subject {subject + 1}: "))
        student_grades.append(mark)
    grades.append(student_grades)

grades_array = np.array(grades)

total_grades = np.sum(grades_array, axis=1)
percentage_array = (total_grades / (number_subjects * 100)) * 100

grades = [calculate_grade(percentage) for percentage in percentage_array]

print("\nResult:")
print("Student\tTotal Grades\tPercentage\tGrade")
for student in range(number_students):
    print(f"{student + 1}\t{total_grades[student]}\t\t{percentage_array[student]:.2f}%\t\t{grades[student]}")
