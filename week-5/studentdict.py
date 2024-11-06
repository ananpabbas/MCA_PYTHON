student={
    'Name': input("Enter the name of the student"),
    'Roll_No': int(input("Enter the roll no of student")),
    'Register_No': int(input("Enter the register no of student")),
    'Department': input("Enter department of student"),
    'Semester': int(input("Enter the sem of student"))
    }
print("Student details",student)
total_mark=int(input("Enter the mark obtained by student out of 100"))
if(total_mark>=90):
    grade="A"
elif(total_mark>=80):
    grade="B"
elif(total_mark>=70):
    grade="C"
elif(total_mark>=60):
    grade="D"
elif(total_mark>=50):
    grade="P"
else:
    grade="F"
student['grade']=grade
print("Updated Student details",student)
del student['Roll_No']
print("After deleting Roll_No",student)
