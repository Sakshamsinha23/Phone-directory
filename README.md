
# 📞 Phone Directory Management System

A **multi-interface** Phone Directory application built using **Python**, **MySQL**, **Tkinter**, **Flask**, and now also available as a **Streamlit Web App**. This system enables users to **add**, **view**, **update**, **delete**, **search**, and even **export** contacts (CLI/GUI). It is ideal for learning full-stack CRUD operations and modern UI integrations.

---

## 🌐 Live Demo

✅ **Streamlit App:** [Phone Directory (Live)](https://phone-directory.streamlit.app/)  
📂 **GitHub Repository:** [GitHub - Sakshamsinha23/phone-directory](https://github.com/Sakshamsinha23/phone-directory)

---

## 🔧 Features

| Feature              | CLI | GUI | Web (Flask) | Web (Streamlit) |
|----------------------|-----|-----|-------------|------------------|
| Add Contact          | ✅  | ✅  | ✅          | ✅               |
| View All Contacts    | ✅  | ✅  | ✅          | ✅               |
| Search Contact       | ✅  | ✅  | ✅          | ✅               |
| Update Contact       | ✅  | ✅  | ✅          | ✅               |
| Delete Contact       | ✅  | ✅  | ✅          | ✅               |
| Export to CSV        | ✅  | ✅  | ❌          | Coming Soon      |
| Form Validation      | ✅  | ✅  | ✅          | ✅               |
| Responsive UI        | 🚫  | ✅  | ✅          | ✅               |

---

## 🗂️ Project Structure

```
📁 phone-directory/
│
├── phone_directory.py         # 📟 CLI App
├── phone_directory_gui.py     # 🪟 Tkinter GUI App
├── app.py                     # 🌐 Flask Web App
├── streamlit_app.py           # 📊 Streamlit Web App
├── .streamlit/secrets.toml    # 🔐 DB credentials for deployment
├── templates/                 # HTML Templates (Flask)
├── static/                    # CSS/JS (Flask)
└── README.md
```

---

## 🛠️ Setup Instructions

### ✅ Requirements

- Python 3.x
- MySQL Server
- Packages: `mysql-connector-python`, `flask`, `tkinter`, `streamlit`, `pandas`

### 🧩 MySQL Setup

```sql
CREATE DATABASE phonebook;

USE phonebook;

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 📦 Install Python Dependencies

```bash
pip install mysql-connector-python flask streamlit pandas
```

---

## 🚀 Run Locally

### 🔹 CLI Version

```bash
python phone_directory.py
```

### 🔹 GUI Version

```bash
python phone_directory_gui.py
```

### 🔹 Flask Web Version

```bash
python app.py
```

Go to `http://127.0.0.1:5000`

### 🔹 Streamlit Version

```bash
streamlit run streamlit_app.py
```

---

## 📸 Screenshots

<details>
<summary>🔽 Web (Streamlit)</summary>

- **Live Directory Interface**

![Streamlit Table View](https://github.com/user-attachments/assets/cfdfe2d7-2dd1-4140-a1cb-caf3fe8677c6)

</details>

<details>
<summary>🔽 GUI App</summary>

- **Tkinter Desktop Interface**

![GUI Interface](https://github.com/user-attachments/assets/026322cc-2bc7-4833-bcdc-6842817a73d1)

</details>

---

## 🔮 Future Enhancements

- 🔐 Admin authentication system
- 📱 Mobile responsive view
- 📤 Export to CSV in Streamlit version
- 📊 Analytics dashboard with usage stats

---

## 🙋‍♂️ Author

**Saksham Sinha**  
📧 sakshamsinha9760@gmail.com  
🔗 [GitHub Profile](https://github.com/Sakshamsinha23)

---

## 📝 License

This project is released under the [MIT License](LICENSE).
