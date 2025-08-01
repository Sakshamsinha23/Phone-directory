
# 📞 Phone Directory Management System

A **multi-interface** Phone Directory application built using **Python**, **MySQL**, **Tkinter**, **Flask**, and now also available as a **Streamlit Web App**. This system enables users to **add**, **view**, **update**, **delete**, **search**, and even **export** contacts (CLI/GUI). It is ideal for learning full-stack CRUD operations and modern UI integrations.

---

## 🌐 Live Demo

✅ **Streamlit App:** [Phone Directory (Live)](https://phone-directory-sam.streamlit.app/)  
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
<img width="1920" height="1080" alt="Screenshot (101)" src="https://github.com/user-attachments/assets/753b79a3-177d-4dd6-8c9b-2e8861ace888" />
<img width="1920" height="1080" alt="Screenshot (100)" src="https://github.com/user-attachments/assets/c667ca40-94cb-40e3-9e0c-11ceb2f6c7c8" />
<img width="1837" height="172" alt="Screenshot 2025-07-30 220134" src="https://github.com/user-attachments/assets/b38257a1-796c-4490-8749-18677b8c4361" />
<img width="1148" height="556" alt="Screenshot 2025-07-30 215255" src="https://github.com/user-attachments/assets/73a498a8-cd62-4b10-b4d2-02176fcdcec1" />

<details>
<summary>🔽 Web (Streamlit)</summary>

🔍 Live Search and Table Refresh

Adding a dynamic search bar in Streamlit and making sure the table updates immediately after actions like Add/Delete required use of st.experimental_rerun() which sometimes led to session glitches.

📦 Project Packaging for GitHub

Organizing files clearly between CLI, GUI, Flask, and Streamlit versions to ensure the README and repo structure remained intuitive for other developers.

- **Live Directory Interface**

![Streamlit Table View](https://github.com/user-attachments/assets/cfdfe2d7-2dd1-4140-a1cb-caf3fe8677c6)

</details>

<details>
<summary>🔽 GUI App</summary>

- **Tkinter Desktop Interface**

![GUI Interface](https://github.com/user-attachments/assets/026322cc-2bc7-4833-bcdc-6842817a73d1)

</details>

---
⚠️ Difficulties Faced
During the development and deployment of the Phone Directory Management System, I encountered several challenges:

🔌 Database Connectivity (MySQL)

Setting up MySQL to work with multiple interfaces (CLI, GUI, Flask, Streamlit) was tricky.
Faced connection errors like Can't connect to MySQL server on 'localhost:3306' during deployment due to remote DB access settings.

🔁 ID Reset Issue After Deletion

Initially tried to reset the id field after contact deletions, but realized it's better to preserve AUTO_INCREMENT for database consistency.

🛡️ Validation and Edge Cases

Ensuring the phone number was always 10 digits and properly validated across all interfaces.
Handling empty form submissions and incorrect input formats required custom validation logic.

☁️ Streamlit Cloud Deployment

Encountered mysql.connector.errors.DatabaseError due to incorrect secrets or database configuration.
Required manual .streamlit/secrets.toml setup and port management for successful connection.

🔍 Live Search and Table Refresh

Adding a dynamic search bar in Streamlit and making sure the table updates immediately after actions like Add/Delete required use of st.experimental_rerun() which sometimes led to session glitches.

📦 Project Packaging for GitHub
Organizing files clearly between CLI, GUI, Flask, and Streamlit versions to ensure the README and repo structure remained intuitive for other developers.

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
