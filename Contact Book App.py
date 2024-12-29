from prettytable import PrettyTable

def display_menu():
    print("\n------ Contact Book App -------")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit the program")

def add_contact():
    user_input = input("\nEnter Name, Number and Email separated by a space: ")
    modified_user_input = user_input.replace(" ",",")
    
    with open("contacts.txt","a") as f: # open in append mode
        f.write(modified_user_input + "\n")
    
    print("✔ Contact Added!\n")
    
def view_contacts():
    
    try:
        with open("contacts.txt","r") as f:
            contacts = f.readlines()
        
        if not contacts:
            print("No contacts found!")
            return

        print("\nAll Contacts:\n")

        # create a table with headers
        table = PrettyTable()
        table.field_names = ["Name", "Phone", "Email"]

        for line in contacts:
                contact = line.strip().split(",")
                name, phone, email = contact
                table.add_row([name, phone, email])
    
        print(table)
        print("\n")
    
    except FileNotFoundError:
        print("No contacts found! File does not exist yet.")
    

def search_contact():
    search_input = input("\nEnter contact name to be searched: ").lower()

    try:
        with open("contacts.txt","r") as f:
            for line in f:
                contact = line.strip().split(",")
                name, phone, email = contact
                if search_input == name.lower():
                    print("Contact Found!")
                    print(f"Name: {name}")
                    print(f"Phone number: {phone}")
                    print(f"Email: {email}")
                    return
        
        print("No such contact :(")
    except FileNotFoundError:
        print("No contacts found! File does not exist yet.")
    

def delete_contact():
    delete_input = input("\nEnter contact name to be deleted: ").lower()
    
    try:
        # read all the lines from the file
        with open("contacts.txt","r") as f:
            contacts = f.readlines() # this give a list, each line

        # find the delete_input name and other than that, write all the lines in a new file
        with open("contacts.txt","w") as f:
            deleted = False # Initialize a flag to track deletion
            for contact in contacts:
                if (delete_input != contact.strip().split(",")[0].lower()):  
                    f.write(contact) # Keep the contact if it doesn’t match the name
                else:
                    deleted = True
            
            if deleted:
                print("Contact deleted!")
            else:
                print("No such contact found!")

    except FileNotFoundError:
        print("No contacts found! File does not exist yet.")
    

while True: # infinite loop until an exit is given
    display_menu()
    user_choice = input("\nSelect the option (1-5): ")

    match user_choice:
        case "1":
            add_contact()
        case "2":
            view_contacts()
        case "3":
            search_contact()
        case "4":
            delete_contact()
        case "5":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice! Please try again.")
