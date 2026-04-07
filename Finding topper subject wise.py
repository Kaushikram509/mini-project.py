#This file main aim is to find topper

# 1. Read total number of students
total_students=int(input("Enter total number of students :"))

#read students marks

telugu_marks=[]
english_marks=[]
hindi_marks=[]
maths_marks=[]
science_marks=[]
social_marks=[]
total_marks=[] #storing each students total marks
students_names=[]#storing students names


for i in range(total_students):
    #for each student read telugu,english,hindi,maths,science and social marks
    name=input("enter students name:")
    students_names.append(name)

    telugu,english,hindi,maths,science,social=map(int,input("Enter marks as per following order telugu,english,hindi,maths,science and social marks :").split())

    #add all subject marks into lists
    telugu_marks.append(telugu)
    english_marks.append(english)
    hindi_marks.append(hindi)
    maths_marks.append(maths)
    science_marks.append(science)
    social_marks.append(social)

    #calculate total
    total=telugu+english+hindi+maths+science+social
    total_marks.append(total)


#find maximum marks
max_marks=max(total_marks)

topper_inds=[]

#find topper indexs and store on list
for i in range(len(total_marks)):
    if total_marks[i]==max_marks:
        topper_inds.append(i)

#print toppers
print("Toppers are :")
for i in topper_inds:
    print(students_names[i])
