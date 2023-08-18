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

number_students = int(input("Enter the number of students: "))
number_subjects = int(input("Enter the number of subjects: "))

grades = []

for student in range(number_students):
    print(f"Enter marks for student {student + 1}:")
    student_marks = []
    for subject in range(number_subjects):
        mark = float(input(f"Subject {subject + 1}: "))
        student_marks.append(mark)
    grades.append(student_marks)

marks_array = np.array(grades)

total_marks = np.sum(marks_array, axis=1)
percentage_array = (total_marks / (number_subjects * 100)) * 100

grades = [calculate_grade(percentage) for percentage in percentage_array]

print("\nResult:")
print("Student\tTotal Marks\tPercentage\tGrade")
for student in range(number_students):
    print(f"{student + 1}\t{total_marks[student]}\t\t{percentage_array[student]:.2f}%\t\t{grades[student]}")
