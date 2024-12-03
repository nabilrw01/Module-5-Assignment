import csv
import os
from contact import Contact

FILENAME = "contacts.csv"

def load_contacts():
    contacts = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(Contact(row['Name'], row['Email'], row['Phone Number'], row['Address']))
    return contacts

def save_contacts(contacts):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['Name', 'Email', 'Phone Number', 'Address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact.__dict__)