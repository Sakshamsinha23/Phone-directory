from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# ✅ MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc123",
    database="phonebook"
)
cursor = db.cursor()

# ✅ Route: View All Contacts
@app.route('/')
def index():
    cursor.execute("SELECT * FROM contacts ORDER BY id DESC")
    contacts = cursor.fetchall()
    return render_template('index.html', contacts=contacts)

# ✅ Route: Add Contact
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        if not name or not phone.isdigit() or len(phone) != 10:
            return "❌ Invalid input! Name required and phone must be exactly 10 digits."

        query = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, phone, email))
        db.commit()
        return redirect(url_for('index'))

    return render_template('add.html')

# ✅ Route: Delete Contact
@app.route('/delete/<int:id>')
def delete_contact(id):
    cursor.execute("DELETE FROM contacts WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('index'))

# ✅ Route: Update Contact
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_contact(id):
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        if not name or not phone.isdigit() or len(phone) != 10:
            return "❌ Invalid input! Name required and phone must be exactly 10 digits."

        query = "UPDATE contacts SET name=%s, phone=%s, email=%s WHERE id=%s"
        cursor.execute(query, (name, phone, email, id))
        db.commit()
        return redirect(url_for('index'))

    # GET request: show form with current contact values
    cursor.execute("SELECT * FROM contacts WHERE id=%s", (id,))
    contact = cursor.fetchone()
    return render_template('update.html', contact=contact)

# ✅ Run the app
if __name__ == '__main__':
    app.run(debug=True)
