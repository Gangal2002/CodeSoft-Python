import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

# ---------------- Functions ----------------
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts():
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def refresh_list(filtered=None):
    """Refresh the listbox showing Name - Phone"""
    listbox.delete(0, tk.END)
    display_contacts = filtered if filtered is not None else contacts
    for contact in display_contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def view_contact_details():
    """Show full contact info in a popup"""
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        details = (
            f"Name: {contact['name']}\n"
            f"Phone: {contact['phone']}\n"
            f"Email: {contact['email']}\n"
            f"Address: {contact['address']}"
        )
        messagebox.showinfo("Contact Details", details)
    else:
        messagebox.showwarning("Warning", "Select a contact to view details!")

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    if not name:
        return

    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    if not phone:
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return

    email = simpledialog.askstring("Add Contact", "Enter Email:") or ""
    address = simpledialog.askstring("Add Contact", "Enter Address:") or ""

    contacts.append({
        "name": name.strip(),
        "phone": phone.strip(),
        "email": email.strip(),
        "address": address.strip()
    })
    save_contacts()
    refresh_list()

def delete_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        confirm = messagebox.askyesno("Delete Contact", f"Delete {contacts[index]['name']}?")
        if confirm:
            contacts.pop(index)
            save_contacts()
            refresh_list()
    else:
        messagebox.showwarning("Warning", "Select a contact to delete!")

def update_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]

        # Ask for each field with pre-filled value
        name = simpledialog.askstring("Update Contact", "Enter Name:", initialvalue=contact['name'])
        phone = simpledialog.askstring("Update Contact", "Enter Phone Number:", initialvalue=contact['phone'])
        email = simpledialog.askstring("Update Contact", "Enter Email:", initialvalue=contact['email'])
        address = simpledialog.askstring("Update Contact", "Enter Address:", initialvalue=contact['address'])

        # Keep old value if user leaves blank or cancels
        if not name:
            name = contact['name']
        if not phone:
            phone = contact['phone']
        if email is None:
            email = contact['email']
        if address is None:
            address = contact['address']

        contacts[index] = {
            "name": name.strip(),
            "phone": phone.strip(),
            "email": email.strip(),
            "address": address.strip()
        }
        save_contacts()
        refresh_list()
    else:
        messagebox.showwarning("Warning", "Select a contact to update!")

def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter Name or Phone:")
    if query:
        filtered = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
        refresh_list(filtered)
    else:
        refresh_list()  # Show all contacts if search is empty/canceled

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("500x500")
root.minsize(450, 450)
root.eval('tk::PlaceWindow . center')

# Heading
tk.Label(root, text="📒 Contact Book", font=("Arial", 20, "bold")).pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add", width=10, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=10, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_contact).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Search", width=10, command=search_contact).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="View Details", width=12, command=view_contact_details).grid(row=0, column=4, padx=5)

# Listbox with Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=75, height=20, font=("Arial", 12), yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

# Load contacts initially
contacts = load_contacts()
refresh_list()

root.mainloop()

