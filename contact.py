class Contact: 
    def __init__(self, name, email, phone_number, address): 
        self.name = name 
        self.email = email 
        self.phone_number = phone_number 
        self.address = address 
    def __str__(self): 
        return f"Name: {self.name}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nAddress: {self.address}\n{'-'*20}" 
    
def display_contacts(contacts): 
    for contact in contacts: 
        print(contact) 
def search_contacts(contacts, search_term): 
    found_contacts = [contact for contact in contacts if search_term.lower() in contact.name.lower() or search_term.lower() in contact.email.lower() or search_term in contact.phone_number or search_term.lower() in contact.address.lower()] 
    return found_contacts