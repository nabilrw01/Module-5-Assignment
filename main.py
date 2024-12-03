from contact import Contact, display_contacts, search_contacts 
from save import load_contacts, save_contacts 
from valid import validate_name, validate_phone_number

def add_contact(contacts):
    try:
        name = input("Enter Name: ")
        validate_name(name)
        email = input("Enter Email: ")
        phone_number = input("Enter Phone Number: ")
        validate_phone_number(phone_number)
        address = input("Enter Address: ")

        for contact in contacts:
            if contact.phone_number == phone_number:
                print("This phone number is already assigned to another contact.")
                return

        new_contact = Contact(name, email, phone_number, address)
        contacts.append(new_contact)
        save_contacts(contacts)
        print("Contact added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def delete_contact(contacts):
    phone_number = input("Enter the phone number of the contact to delete: ")
    updated_contacts = [contact for contact in contacts if contact.phone_number != phone_number]
    
    if len(contacts) == len(updated_contacts):
        print("No contact found with the provided phone number.")
    else:
        save_contacts(updated_contacts)
        print("Contact deleted successfully!")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Delete Contact")
        print("4. Search Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_term = input("Enter name, email, phone number, or address to search: ")
            found_contacts = search_contacts(contacts, search_term)
            if found_contacts:
                display_contacts(found_contacts)
            else:
                print("No contacts found matching the search term.")
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()