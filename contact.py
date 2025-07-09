def add_contact(name ,phone):
    if name in contact:
        print(f"Contact {name} already exists in data.")
    else:
        contact[name] =phone
        print(f"Contact {name} added with phone number {phone}.")

def delete_contact(name):
    if name in contact:
        del contact[name]
        print(f"Contact {name} deleted.")
    else :
        print(f"contact{name} does not exist.")

def view_contacts(name):
    if name in contact:
        print(f"Contact {name} has phone number {contact[name]}.")
    else:
        print(f"Contact {name} does not exist.")

def view_all_contact():
    if contact:
        print("all contacts:")
        for name,phone in contact.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")

def save_contacts():
    """ save contacts to a file """
    with open("contact.txt","w") as file:
        for name , phone in contact.items():
            file.write(f"{name},{phone}\n")
    print("Contacts saved to contact.txt.") 


contact={}

try:
    try:
        with open("contact.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(',')
                contact[name] = phone
    except FileNotFoundError:
        contact_item=int(input("Enter the number of contacts you want to add: "))
        for i in range(contact_item):
            name = input(f"Enter contact name:{i+1} ")
            phone = input(f"Enter phone number for {name} ")
            contact[name] = phone
except ValueError:
    print("Invalid input. Please enter a valid number of contacts.")    

while True:
    operation = input("Enter operation (add, delete, view, view_all, exit): ")
    match operation.lower():
        case "add":
            name = input("Enter contact name to add: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)

        case "delete":
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        
        case "view":
            name = input("Enter contact name to view: ")
            view_contacts(name)

        case "view_all":
            view_all_contact()

        case "exit":
            save_contacts()
            print("Exiting contact book.")
            break

        case _:
            print("Invalid operation. Please choose from add, delete, view, view_all, or exit.")
