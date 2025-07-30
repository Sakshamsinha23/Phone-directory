import streamlit as st
import mysql.connector
import pandas as pd

# ✅ Database connection
db = mysql.connector.connect(
    host=st.secrets["DB_HOST"],
    user=st.secrets["DB_USER"],
    password=st.secrets["DB_PASSWORD"],
    database=st.secrets["DB_NAME"],
    port=int(st.secrets["DB_PORT"])
)
cursor = db.cursor()

# ✅ Page setup
st.set_page_config("📞 Phone Directory", layout="centered")
st.title("📞 Phone Directory")
st.markdown("---")

# ✅ Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(15),
        email VARCHAR(100)
    )
""")
db.commit()

# ✅ Add contact form
with st.form("add_contact"):
    st.subheader("➕ Add New Contact")
    name = st.text_input("Name")
    phone = st.text_input("Phone (10 digits)")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Add Contact")

    if submitted:
        if not name or not phone.isdigit() or len(phone) != 10:
            st.error("❌ Invalid input! Name required and phone must be 10 digits.")
        else:
            cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
            db.commit()
            st.success("✅ Contact added!")

# ✅ View contacts
st.subheader("📋 All Contacts")
cursor.execute("SELECT * FROM contacts ORDER BY id DESC")
rows = cursor.fetchall()

if rows:
    df = pd.DataFrame(rows, columns=["ID", "Name", "Phone", "Email"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("No contacts available.")

# ✅ Delete contact
st.subheader("❌ Delete Contact")
delete_id = st.text_input("Enter ID to delete")
if st.button("Delete"):
    if delete_id.isdigit():
        cursor.execute("DELETE FROM contacts WHERE id = %s", (delete_id,))
        db.commit()
        st.success("✅ Contact deleted!")
    else:
        st.error("Please enter a valid numeric ID.")

# ✅ Update contact
st.subheader("✏️ Update Contact")
update_id = st.text_input("Enter ID to update")
if update_id and update_id.isdigit():
    cursor.execute("SELECT * FROM contacts WHERE id = %s", (update_id,))
    contact = cursor.fetchone()
    if contact:
        with st.form("update_form"):
            new_name = st.text_input("Name", value=contact[1])
            new_phone = st.text_input("Phone", value=contact[2])
            new_email = st.text_input("Email", value=contact[3])
            update_btn = st.form_submit_button("Update Contact")

            if update_btn:
                if not new_name or not new_phone.isdigit() or len(new_phone) != 10:
                    st.error("❌ Invalid input.")
                else:
                    cursor.execute("UPDATE contacts SET name=%s, phone=%s, email=%s WHERE id=%s",
                                (new_name, new_phone, new_email, update_id))
                    db.commit()
                    st.success("✅ Contact updated!")
    else:
        st.warning("⚠️ No contact found with this ID.")
