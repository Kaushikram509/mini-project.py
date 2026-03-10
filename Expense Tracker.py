expenses = []
choice = 0

while True:
    print("Add Expenes")
    print("View Expenes")
    print("Total Expenes")
    print("Exit")

    choice = int(input())
    if(choice==1):
        amount = int(input("Enter amount: "))
        expenses.append(amount)
    elif(choice==2):
        for exp in expenses:
            print(exp)
    elif(choice==3):
        total = sum(expenses)
        print(total)
    elif(choice==4):
        print("Exit")
        break
    else:
        print("Invalid input")
    
