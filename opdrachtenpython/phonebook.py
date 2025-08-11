import json
import os

FILE_NAME = "contactinfo.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, dict):
                    return data
            except json.JSONDecodeError:
                pass
    return {}

def save_contacts(contact):
    sorted_contacts = dict(sorted(contact.items(), key=sort_key))
    with open(FILE_NAME, "w") as file:
        json.dump(sorted_contacts, file, indent=4)

def normalize_name(name):
    return name.strip().lower()

def find_contact_key(contact, name):
    norm_name = normalize_name(name)
    for stored_name in contact.keys():
        if normalize_name(stored_name) == norm_name:
            return stored_name
    return None

def sort_key(item):
    # item is a tuple (name, data)
    return item[0].lower()

def welcome():
    while True:
        try:
            entry = int(input("""
Welcome to Py Contact Book  
---------------------------------
Py Contact Book commands:
1. Display your existing contacts
2. Create a new contact
3. Check an entry (exact name)
4. Search contacts by partial name
5. Edit an existing contact's phone or email
6. Change a contact's name
7. Delete an entry
8. Exit
---------------------------------
Enter your choice (1-8): """))
            if entry in range(1, 9):
                return entry
            else:
                print("Please enter a number between 1 and 8.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.")

def display_contacts(contact):
    if contact:
        print("\nYour contacts (sorted alphabetically):")
        for k, v in sorted(contact.items(), key=sort_key):
            print(f"{k} | Email: {v['email']} | Phone: {v['phone']}")
    else:
        print("\nYou have an empty phonebook! Add a new contact from the menu.")

def create_contact(contact):
    contact_name = input("Save as (FirstName, LastName): ").strip()
    email_address = input("Please enter an email address: ").strip()
    phone_number = input("Please enter a number: ").strip()
    
    if phone_number in (c['phone'] for c in contact.values()):
        print("That phone number already exists in your phonebook.")
        return
    if email_address in (c['email'] for c in contact.values()):
        print("That email address already exists in your phonebook.")
        return
    if find_contact_key(contact, contact_name):
        print("That name already exists in your phonebook.")
        return
    
    contact[contact_name] = {"phone": phone_number, "email": email_address}
    save_contacts(contact)
    print("\nContact successfully saved!")
    display_contacts(contact)

def check_entry(contact):
    name = input("Enter the exact name to view details: ").strip()
    key = find_contact_key(contact, name)
    if key:
        v = contact[key]
        print(f"The contact is {key} | Email: {v['email']} | Phone: {v['phone']}")
    else:
        print("That contact does not exist.")

def search_contacts_partial(contact):
    query = input("Enter partial name to search for: ").strip().lower()
    matches = {k: v for k, v in contact.items() if query in k.lower()}
    if matches:
        print(f"\nContacts matching '{query}':")
        for k, v in sorted(matches.items(), key=sort_key):
            print(f"{k} | Email: {v['email']} | Phone: {v['phone']}")
    else:
        print(f"No contacts found containing '{query}'.")

def edit_contact(contact):
    name = input("Enter the exact name of the contact to edit: ").strip()
    key = find_contact_key(contact, name)
    if not key:
        print("That contact does not exist.")
        return
    
    v = contact[key]
    print(f"Current details for {key} | Email: {v['email']} | Phone: {v['phone']}")
    
    choice = input("What would you like to edit? Enter 'phone' or 'email': ").strip().lower()
    
    if choice == 'phone':
        new_number = input("Enter the new phone number: ").strip()
        if new_number in (c['phone'] for k, c in contact.items() if k != key):
            print("That phone number is already assigned to another contact.")
            return
        contact[key]['phone'] = new_number
        save_contacts(contact)
        print(f"Contact {key} phone number updated successfully!")
    
    elif choice == 'email':
        new_email = input("Enter the new email address: ").strip()
        if new_email in (c['email'] for k, c in contact.items() if k != key):
            print("That email address is already assigned to another contact.")
            return
        contact[key]['email'] = new_email
        save_contacts(contact)
        print(f"Contact {key} email address updated successfully!")
    
    else:
        print("Invalid choice. Please enter 'phone' or 'email'.")

def change_contact_name(contact):
    old_name = input("Enter the exact current name of the contact: ").strip()
    key = find_contact_key(contact, old_name)
    if not key:
        print("That contact does not exist.")
        return
    
    new_name = input("Enter the new name for this contact: ").strip()
    if find_contact_key(contact, new_name):
        print("That new name already exists in the phonebook.")
        return
    
    contact[new_name] = contact.pop(key)
    save_contacts(contact)
    print(f"Contact name changed from '{key}' to '{new_name}' successfully!")

def delete_entry(contact):
    name = input("Enter the exact name to delete: ").strip()
    key = find_contact_key(contact, name)
    if key:
        v = contact[key]
        print(f"The contact is {key} | Email: {v['email']} | Phone: {v['phone']}")
        confirm = input("Are you sure you wish to delete this contact? Yes/No: ").strip().lower()
        if confirm == "yes":
            contact.pop(key)
            save_contacts(contact)
            print("Contact deleted.")
            if contact:
                display_contacts(contact)
            else:
                print("The phonebook is now empty.")
        else:
            print("Deletion cancelled.")
    else:
        print("That contact does not exist.")

def exit_program():
    print("Goodbye OwO")
    return True

def phonebook():
    contact = load_contacts()
    while True:
        entry = welcome()
        if entry == 1:
            display_contacts(contact)
        elif entry == 2:
            create_contact(contact)
        elif entry == 3:
            check_entry(contact)
        elif entry == 4:
            search_contacts_partial(contact)
        elif entry == 5:
            edit_contact(contact)
        elif entry == 6:
            change_contact_name(contact)
        elif entry == 7:
            delete_entry(contact)
        elif entry == 8:
            if exit_program():
                break

phonebook()

