#fee calculator based on course and marks

def calculate_fee(course, marks):
    if(course=="AI"):
        fee = 50000
    elif(course=="Web"):
        fee = 40000
    else:
        return None
    
    #Discount Condition
    if(marks>90):
        fee -= 5000
    return fee

def main():
    course = input("Enter the course: ")
    marks = int(input("Enter the marks: ")) 

    fee = calculate_fee(course, marks)

    if(fee is None):
        print("Invalid course Selected")
    else:
        print("Final fee:",fee)
main()
