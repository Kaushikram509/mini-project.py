expenses = []
def export_expenses(expenses):
    with open("expenses.txt","w") as file:
        for expense in expenses:
            file.write(expense["name"] + " " + str(expense["amount"]) + "\n")
def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expense")
        print("3. Export to file")
        print("4. Exit")

        choice = input("Enter choice: ")
        if(choice=="1"):
            name = input("Enter expense name: ")
            amount = int(input("Enter amount: "))

            expenses.append({"name":name,"amount":amount})
        elif(choice=="2"):
            for expense in expenses:
                print(expense["name"], "-",expense["amount"])

        elif(choice=="3"):
            export_expenses(expenses)
        elif(choice=="4"):
            print("Exiting the prgm")
            break
        else:
            print("Invalid choice. Try again")
def load_expenses():
    try:
        with open(r"C:\Users\T.kaushik ram\OneDrive\Desktop\DSA python codes\expenses.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split()
                expenses.append({"name": name, "amount": int(amount)})
    except FileNotFoundError:
        pass
load_expenses()
main()
