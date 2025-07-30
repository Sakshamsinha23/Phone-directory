import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import csv

# ✅ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc123",
    database="phonebook"
)
cursor = conn.cursor()

# ✅ Add Contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if not name or not phone.isdigit() or not (7 <= len(phone) <= 15):
        messagebox.showerror("Invalid Input", "Name must not be empty and phone must be 7–15 digits.")
        return
    if email and "@" not in email:
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    try:
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
        conn.commit()
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        load_contacts()
    except mysql.connector.IntegrityError:
        messagebox.showerror("Duplicate", "Phone number already exists.")

# ✅ Load contacts into TreeView
def load_contacts():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT id, name, phone, email, date_added FROM contacts")
    for contact in cursor.fetchall():
        tree.insert("", "end", values=contact)

# ✅ Clear form
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# ✅ Search contact
def search_contact(term):
    for row in tree.get_children():
        tree.delete(row)

    query = "SELECT * FROM contacts WHERE name LIKE %s OR phone LIKE %s"
    cursor.execute(query, (f"%{term}%", f"%{term}%"))
    results = cursor.fetchall()

    if results:
        for contact in results:
            tree.insert("", "end", values=contact)
    else:
        messagebox.showinfo("No Results", "No matching contact found.")

# ✅ Delete selected contact
def delete_contact():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")
        return

    data = tree.item(selected_item)["values"]
    contact_id = data[0]

    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{data[1]}'?")
    if confirm:
        cursor.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
        conn.commit()
        load_contacts()
        messagebox.showinfo("Deleted", "Contact deleted successfully.")

# ✅ Fill form from selected row for update
def fill_form_from_selection():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("No Selection", "Please select a contact to update.")
        return

    data = tree.item(selected_item)["values"]
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    entry_name.insert(0, data[1])
    entry_phone.insert(0, data[2])
    entry_email.insert(0, data[3])

    # Store ID for update
    update_button.config(state=tk.NORMAL)
    update_button.contact_id = data[0]

# ✅ Update selected contact
def update_contact():
    contact_id = update_button.contact_id
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if not name or not phone.isdigit() or not (7 <= len(phone) <= 15):
        messagebox.showerror("Invalid Input", "Name must not be empty and phone must be 7–15 digits.")
        return
    if email and "@" not in email:
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    try:
        cursor.execute("UPDATE contacts SET name=%s, phone=%s, email=%s WHERE id=%s", (name, phone, email, contact_id))
        conn.commit()
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
        load_contacts()
        update_button.config(state=tk.DISABLED)
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Update failed: {e}")

# ✅ Export contacts to CSV
def export_to_csv():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    if not rows:
        messagebox.showinfo("No Data", "No contacts to export.")
        return

    with open("contacts_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Phone", "Email", "Date Added"])
        writer.writerows(rows)

    messagebox.showinfo("Exported", "Contacts exported to 'contacts_export.csv'.")

# ✅ GUI Setup
root = tk.Tk()
root.title("📞 Phone Directory")
root.geometry("860x540")
root.resizable(False, False)

# 🔹 Entry Frame
frame = tk.LabelFrame(root, text="Add / Update Contact", padx=10, pady=10)
frame.pack(pady=10, padx=10, fill="x")

tk.Label(frame, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Phone:").grid(row=1, column=0)
entry_phone = tk.Entry(frame, width=30)
entry_phone.grid(row=1, column=1, padx=10)

tk.Label(frame, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(frame, width=30)
entry_email.grid(row=2, column=1, padx=10)

# Buttons
tk.Button(frame, text="Add Contact", command=add_contact).grid(row=3, column=1, pady=10, sticky="w")
update_button = tk.Button(frame, text="Update Contact", command=update_contact, state=tk.DISABLED)
update_button.grid(row=3, column=1, pady=10, sticky="e")

# 🔹 Treeview
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

columns = ("ID", "Name", "Phone", "Email", "Date Added")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=140 if col != "Email" else 180)

tree.pack()

# 🔹 Controls
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Label(control_frame, text="Search:").grid(row=0, column=0, padx=5)
search_entry = tk.Entry(control_frame, width=30)
search_entry.grid(row=0, column=1, padx=5)

tk.Button(control_frame, text="Search", command=lambda: search_contact(search_entry.get())).grid(row=0, column=2, padx=5)
tk.Button(control_frame, text="Show All", command=load_contacts).grid(row=0, column=3, padx=5)
tk.Button(control_frame, text="Delete Selected", command=delete_contact).grid(row=0, column=4, padx=5)
tk.Button(control_frame, text="Edit Selected", command=fill_form_from_selection).grid(row=0, column=5, padx=5)
tk.Button(control_frame, text="Export to CSV", command=export_to_csv).grid(row=0, column=6, padx=5)

# 🔄 Load contacts
load_contacts()

# ✅ Start GUI loop
root.mainloop()
