students = set()

while True:
    student = input("Enter student name (or enter 'end') ")
    if student.lower() == "end":
        break
    students.add(student)
    print(f"{student} added to list.")
    
print("Student who go to journey, list:", students)