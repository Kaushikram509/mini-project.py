def calculator(a,b):
    addition = a+b
    print(addition)
    print("----------------------------------------------")
    subtraction = a-b
    print(subtraction)
    print("----------------------------------------------")
    multiplication = a*b
    print(multiplication)
    print("----------------------------------------------")
    if(b!=0):
        division = a/b
        print(division)
    else:
        print("The value is invalid....")
        print("----------------------------------------------")
a = int(input())
b = int(input())
print(calculator(a,b))
