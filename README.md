# Phone-directory
📞 A complete Phone Directory web application built using Python, MySQL, and Flask. It allows users to add, view, update, and delete contacts with validation and timestamp tracking. Ideal for learning CRUD operations, full-stack development, and deployment on platforms on Heroku

# 📞 Phone Directory Management System

A versatile, multi-interface Phone Directory application built with Python, MySQL, Tkinter, and Flask. This system allows users to **add**, **view**, **update**, **delete**, **search**, and **export** contacts. Designed with usability in mind, the project supports three powerful interfaces:

- 🖥️ **CLI Version** (Console-based interaction)
- 🪟 **GUI Version** (Tkinter desktop app)
- 🌐 **Web Version** (Flask + Bootstrap)

---

## 🔧 Features

| Feature              | CLI | GUI | Web |
|----------------------|-----|-----|-----|
| Add Contact          | ✅  | ✅  | ✅  |
| View All Contacts    | ✅  | ✅  | ✅  |
| Search Contact       | ✅  | ✅  | ✅  |
| Update Contact       | ✅  | ✅  | ✅  |
| Delete Contact       | ✅  | ✅  | ✅  |
| Export to CSV        | ✅  | ✅  | 🚫  |
| Form Validation      | ✅  | ✅  | ✅  |
| Responsive UI        | 🚫  | ✅  | ✅  |

---

## 🗂️ Project Structure

```
📁 phone-directory/
│
├── phone_directory.py         # 📟 CLI App
├── phone_directory_gui.py     # 🪟 Tkinter GUI App
├── app.py                     # 🌐 Flask Web App (Backend + Routes)
├── templates/
│   ├── add.html               # ➕ Web Add Contact Page
│   └── update.html            # ✏️ Web Update Contact Page
├── static/                    # (Optional for CSS/JS if extended)
└── README.md
```

---

## 🛠️ Setup Instructions

### 📋 Requirements
- Python 3.x
- MySQL Server
- Python Packages: `mysql-connector-python`, `Flask`, `tkinter` (standard)

### 🧩 MySQL Setup

```sql
CREATE DATABASE phonebook;

USE phonebook;

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(100),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 💡 Install Dependencies

```bash
pip install mysql-connector-python flask
```

---

## 🚀 How to Run

### 🔹 CLI Version

```bash
python phone_directory.py
```

### 🔹 GUI Version

```bash
python phone_directory_gui.py
```

### 🔹 Web Version (Flask)

```bash
python app.py
```

Then open your browser and go to:  
`http://127.0.0.1:5000`

---

## 📸 Screenshots

<details>
<summary>🔽 Web App</summary>

- **Add Contact Page**

![Add Contact](https://via.placeholder.com/600x300?text=Add+Contact+Page)

- **Update Contact Page**

![Update Contact](https://via.placeholder.com/600x300?text=Update+Contact+Page)

</details>

<details>
<summary>🔽 GUI App</summary>

- **Tkinter Interface**

![GUI App](https://via.placeholder.com/600x300?text=Tkinter+Interface)

</details>

---

## 💡 Future Improvements

- 🔐 User authentication (login/logout)
- 📱 Mobile responsive web design
- ☁️ Cloud deployment (e.g. Vercel, Heroku)
- 🔔 Toast notifications and real-time alerts
- 📊 Analytics on contact usage

---

## 🙋‍♂️ Author

**Saksham Sinha**  
📧 sakshamsinha9760@gmail.com 
🔗 [GitHub](https://github.com/Sakshamsinha23)

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
