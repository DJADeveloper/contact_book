import json
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

# Global contact book list
contact_book = []

# Load contacts from a JSON file
def load_contacts():
    global contact_book
    if os.path.exists('contacts.json'):
        with open('contacts.json', 'r') as file:
            contact_book = json.load(file)

# Save contacts to a JSON file
def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contact_book, file, indent=4)

# Add a new contact
def add_contact_gui():
    contact_name = simpledialog.askstring("Input", "Name of Contact:")
    contact_number = simpledialog.askstring("Input", "New contact number:")
    if contact_name and contact_number:
        new_contact = {"name": contact_name, "number": contact_number}
        contact_book.append(new_contact)
        save_contacts()
        messagebox.showinfo("Info", f'Contact {contact_name} added.')
    else:
        messagebox.showerror("Error", "Both name and number are required.")

# View all contacts
def view_contacts_gui():
    contact_list = "\n".join([f'{contact["name"]}: {contact["number"]}' for contact in contact_book])
    messagebox.showinfo("Contacts", contact_list or 'No contacts available.')

# Remove a contact
def remove_contact_gui():
    contact_name = simpledialog.askstring("Input", "Who would you like to remove?")
    for contact in contact_book:
        if contact["name"] == contact_name:
            contact_book.remove(contact)
            save_contacts()
            messagebox.showinfo("Info", f'Contact {contact_name} removed.')
            return
    messagebox.showerror("Error", f'Contact {contact_name} not found.')

# Update a contact
def update_contact_gui():
    contact_name = simpledialog.askstring("Input", "Enter the name of the contact you want to update:")
    for contact in contact_book:
        if contact["name"] == contact_name:
            new_name = simpledialog.askstring("Input", f'Enter new name for {contact_name} (press Enter to skip):')
            new_number = simpledialog.askstring("Input", f'Enter new number for {contact_name} (press Enter to skip):')
            if new_name:
                contact["name"] = new_name
            if new_number:
                contact["number"] = new_number
            save_contacts()
            messagebox.showinfo("Info", f'Contact {contact_name} updated.')
            return
    messagebox.showerror("Error", f'Contact {contact_name} not found.')

# Search for a contact
def search_contact_gui():
    search_term = simpledialog.askstring("Input", "Enter name or number to search:")
    results = [contact for contact in contact_book if search_term.lower() in contact["name"].lower() or search_term in contact["number"]]
    if results:
        contact_list = "\n".join([f'{contact["name"]}: {contact["number"]}' for contact in results])
        messagebox.showinfo("Search Results", contact_list)
    else:
        messagebox.showinfo("Search Results", 'No matching contacts found.')

# Tkinter setup
def main():
    load_contacts()
    
    root = tk.Tk()
    root.title("Contact Book")
    frame = tk.Frame(root)
    frame.pack(pady=10)

    add_button = tk.Button(frame, text="Add Contact", command=add_contact_gui)
    add_button.pack(pady=5)

    view_button = tk.Button(frame, text="View Contacts", command=view_contacts_gui)
    view_button.pack(pady=5)

    remove_button = tk.Button(frame, text="Remove Contact", command=remove_contact_gui)
    remove_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Contact", command=update_contact_gui)
    update_button.pack(pady=5)

    search_button = tk.Button(frame, text="Search Contact", command=search_contact_gui)
    search_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
