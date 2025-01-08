
student = {}

n = int(input("Enter the number of students: "))

for i in range(n):
    name = input(f"Enter the name of student {i+1}: ")
    marks = float(input(f"Enter the marks of {name}: "))
    student[name] = marks
sorted_student = dict(sorted(student.items(), key=lambda item: item[0], reverse=True))
print("\nStudent list sorted by names in descending order:")
for name, marks in sorted_student.items():
    print(f"{name}: {marks}")
