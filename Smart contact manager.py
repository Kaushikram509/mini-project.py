# Smart Contact Manager

contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print()

def search_contact():
    search_name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(" Found:", contact['name'] - contact['phone'])
            found = True
            break
    if not found:
        print(" Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(" Contact deleted successfully!\n")
            return
    print(" Contact not found.\n")

# Main Menu
while True:
    print("====== Smart Contact Manager ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print(" Exiting program...")
        break
    else:
        print(" Invalid choice. Try again.\n")
