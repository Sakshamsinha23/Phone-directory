import mysql.connector
import csv
import re
from datetime import datetime

# ✅ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc123",
    database="phonebook"
)
cursor = conn.cursor()

# ✅ Validators
def is_valid_phone(phone):
    return phone.isdigit() and 7 <= len(phone) <= 15

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# ✅ Add Contact
def add_contact():
    name = input("Enter name: ").strip()
    if not name:
        print("❌ Name cannot be empty.\n")
        return

    phone = input("Enter phone number: ").strip()
    if not is_valid_phone(phone):
        print("❌ Invalid phone number. Digits only (7-15).\n")
        return

    email = input("Enter email (optional): ").strip()
    if email and not is_valid_email(email):
        print("❌ Invalid email format.\n")
        return

    try:
        cursor.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)",
            (name, phone, email)
        )
        conn.commit()
        print("✅ Contact added successfully!\n")
    except mysql.connector.IntegrityError:
        print("⚠️ Phone number already exists.\n")

# ✅ View Contacts
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    if rows:
        print("\n📒 Contact List:")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]} | Added: {row[4]}")
    else:
        print("📭 No contacts found.\n")

# ✅ Search Contacts
def search_contact():
    term = input("Enter name or phone to search: ").strip()
    cursor.execute(
        "SELECT * FROM contacts WHERE name LIKE %s OR phone LIKE %s",
        (f"%{term}%", f"%{term}%")
    )
    results = cursor.fetchall()

    if results:
        print("\n🔍 Search Results:")
        for r in results:
            print(f"ID: {r[0]} | Name: {r[1]} | Phone: {r[2]} | Email: {r[3]} | Added: {r[4]}")
    else:
        print("❌ No matching contact found.\n")

# ✅ Update Contact
def update_contact():
    contact_id = input("Enter contact ID to update: ").strip()
    cursor.execute("SELECT * FROM contacts WHERE id=%s", (contact_id,))
    record = cursor.fetchone()

    if not record:
        print("❌ Contact not found.\n")
        return

    print(f"\nCurrent details - Name: {record[1]}, Phone: {record[2]}, Email: {record[3]}")
    confirm = input("Proceed with update? (y/n): ").strip().lower()
    if confirm != 'y':
        print("🔁 Update cancelled.\n")
        return

    new_name = input("New name: ").strip()
    new_phone = input("New phone: ").strip()
    new_email = input("New email: ").strip()

    if not new_name or not is_valid_phone(new_phone) or (new_email and not is_valid_email(new_email)):
        print("❌ Invalid input(s). Please check again.\n")
        return

    try:
        cursor.execute(
            "UPDATE contacts SET name=%s, phone=%s, email=%s WHERE id=%s",
            (new_name, new_phone, new_email, contact_id)
        )
        conn.commit()
        print("✅ Contact updated successfully!\n")
    except mysql.connector.Error as e:
        print(f"⚠️ Update failed: {e}\n")

# ✅ Delete Contact
def delete_contact():
    contact_id = input("Enter contact ID to delete: ").strip()
    cursor.execute("SELECT * FROM contacts WHERE id=%s", (contact_id,))
    record = cursor.fetchone()

    if not record:
        print("❌ Contact not found.\n")
        return

    confirm = input(f"Are you sure you want to delete '{record[1]}'? (y/n): ").strip().lower()
    if confirm == 'y':
        cursor.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
        conn.commit()
        print("🗑️ Contact deleted.\n")
    else:
        print("🔁 Deletion cancelled.\n")

# ✅ Export to CSV
def export_to_csv():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    if not rows:
        print("📭 No contacts to export.\n")
        return

    with open("contacts_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Phone", "Email", "Date Added"])
        writer.writerows(rows)

    print("✅ Exported to 'contacts_export.csv'\n")

# ✅ Menu
def main():
    while True:
        print("\n📞 Phone Directory Menu")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export Contacts to CSV")
        print("7. Exit")

        choice = input("Choose an option (1–7): ").strip()
        print()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            export_to_csv()
        elif choice == '7':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

    cursor.close()
    conn.close()

# ✅ Run App
if __name__ == "__main__":
    main()
