"""finding the topper in the class by using of dictionary"""
n = int(input("Enter the number of students: "))
students={}
for i in range(n):
    name = input("Enter the name: ")
    marks = int(input("Enter the marks of student: "))
    students[name]=marks
topper=" "
max_marks=0
for name,marks in students.items():
    if(marks>max_marks):
        max_marks=marks
        topper=name
print("Topper is: ",topper)
print("Marks: ",max_marks)
