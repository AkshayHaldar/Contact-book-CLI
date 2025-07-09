def add_contact(name, phone):
    if name in contact:
        print(f"----- Name already Exists -----")
        print(f"contact {name} already exists with phone number: {contact[name]}")
        
        update_phone = input(f"Do you want to update '{name}' with the new number {phone}? (yes/no): ").strip().lower()
        if update_phone== "yes" or update_phone=="y":
            contact[name] = phone
            print(f"Success! Contact {name} has been updated with phone number {contact[name]}.")
        else:
            print("Operation cancelled. No changes were made.")
        return
    # --- Case 2: The PHONE NUMBER already exists (but the name is new). ---
    already_name = None
    for n, p in contact.items():
        if p == phone:
            already_name = n
            break # Found a match, stop searching

    if already_name:
        print(f"------ Phone Number Exists-- ---")
        print(f"The phone number {phone} is already assigned to the contact {already_name}.")
        
        # Give the user clear options
        change_name = input("What operation you want to do? (replace / edit / cancel): ").strip().lower()

        if change_name == "replace":
            # This replaces the old contact with the new one
            del contact[already_name]
            contact[name] = phone
            print(f"Success! Deleted '{already_name}' and added '{name}' with number {phone}.")
        
        elif change_name == "edit":
            print(f"You are editing the name for the existing contact '{already_name}'.")
            new_name = input(f"Enter the new name for the contact with number {phone}: ")
            if new_name in contact:
                print(f"Error: A contact named '{new_name}' already exists. No changes made.")
            else:
                del contact[already_name]
                contact[new_name] = phone
                print(f"Success! Contact name changed from '{already_name}' to '{new_name}'.")
        else:
            print("nothing is changed, contact is remains same")
        return

    # --- Case 3: Both name and phone are new. ---
    contact[name] = phone
    print(f"Success! Contact '{name}' added with phone number {phone}.")
      

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
        with open("contact.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(',')
                contact[name] = phone
except ValueError:
    print("Invalid input. Please enter a valid number of contacts.")    

while True:
    """Make sure to save your contact in contact.txt you have to exit your file by typing exit"""
    operation = input("Enter operation (add, delete, view, view_all, exit): ").lower().strip()
    match operation:
        case "add":
            contact_item=int(input("Enter the number of contacts you want to add: "))
            for i in range(contact_item):
              name = input(f"Enter contact name {i+1}: ")
              phone = input(f"Enter phone number for {name} (10 digits): ")
              if len(phone) == 10 and phone.isalnum():
                add_contact(name, phone)
              else:
                print("Invalid phone number. Please enter a 10-digit number.")
              
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
