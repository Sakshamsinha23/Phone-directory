import streamlit as st
import mysql.connector
import pandas as pd

# ✅ Page Setup
st.set_page_config("📞 Phone Directory", layout="wide")

# ✅ Connect to DB
db = mysql.connector.connect(
    host=st.secrets["DB_HOST"],
    user=st.secrets["DB_USER"],
    password=st.secrets["DB_PASSWORD"],
    database=st.secrets["DB_NAME"],
    port=int(st.secrets["DB_PORT"])
)
cursor = db.cursor()

# ✅ Create contacts table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(15),
        email VARCHAR(100)
    )
""")
db.commit()

# ✅ Title & Search Row
col1, col2 = st.columns([4, 2])
with col1:
    st.title("📞 Phone Directory")
with col2:
    search_term = st.text_input("🔍 Search", placeholder="Name / Phone / Email")

# ✅ Add Contact Form
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
            st.experimental_rerun()

# ✅ Show All Contacts (after search filter)
st.subheader("📋 All Contacts")
cursor.execute("SELECT * FROM contacts ORDER BY id DESC")
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=["ID", "Name", "Phone", "Email"])

if search_term:
    df = df[df.apply(lambda row: search_term.lower() in str(row["Name"]).lower()
                                 or search_term in str(row["Phone"])
                                 or search_term.lower() in str(row["Email"]).lower(), axis=1)]

if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("No contacts match your search." if search_term else "No contacts available.")

# ✅ Delete Contact
st.subheader("❌ Delete Contact")
delete_id = st.text_input("Enter ID to delete")
if st.button("Delete"):
    if delete_id.isdigit():
        cursor.execute("DELETE FROM contacts WHERE id = %s", (delete_id,))
        db.commit()
        st.success("✅ Contact deleted!")
        st.experimental_rerun()
    else:
        st.error("Please enter a valid numeric ID.")

# ✅ Update Contact
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
                    st.experimental_rerun()
    else:
        st.warning("⚠️ No contact found with this ID.")
