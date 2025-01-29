student_grades = {}
while True:
    name = input("Enter Student name (or write 'end'): ")
    if name.lower() == "end":
        break
    grade = int(input("Enter mark: "))
    student_grades[name] = grade

if len(student_grades) > 0:
    total_grades = sum(student_grades.values())
    num_students = len(student_grades)
    average_grade = total_grades / num_students
else:
    average_grade = 0 
print(f"All studens average mark: {average_grade:}")

students_to_remove = []
for name, grade in student_grades.items():
    if grade < 80:
        students_to_remove.append(name)

for student in students_to_remove:
    del student_grades[student]

while True:
    student_to_check = input("Enter Name to check (or enter 'end'): ")
    if student_to_check.lower() == "end":
        break
    if student_to_check in student_grades:
        print(f"{student_to_check} found. Mark: {student_grades[student_to_check]:}")
    else:
        print(f"{student_to_check} not found.")