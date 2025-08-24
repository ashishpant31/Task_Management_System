**🤖 Try:** https://ashish-task-management.streamlit.app/

# 📈 Task Management System

## 📖 About

**Task Management System** is a simple, intuitive web app built with [Streamlit](https://streamlit.io) and SQLite. It enables both personal and team task management, allowing you to create, edit, prioritize, and track tasks easily through a clean interface.

---

## ✨ Features

- **Task Management:** Add, edit, and update tasks with details including title, description, priority, status, and optional deadlines.
- **Clear UI:** Active and completed tasks are displayed separately for better organization.
- **Easy Editing:** Click on active tasks to edit; completed tasks are read-only.
- **Intelligent Sorting:** Active tasks are automatically ranked by priority and deadline.
- **Persistent Storage:** All data is saved securely in a local SQLite database.
- **Export Capability:** Optionally export your tasks to CSV for offline review.
- **Responsive UI:** Minimal and responsive design powered by Streamlit.

---

## 🖼️ Screenshots

### Task Management UI – Active and Completed Tasks

<p align="center">
  <img width="1493" height="728" alt="Task Manager Screenshot 1" src="https://github.com/user-attachments/assets/ab750486-c96b-4b42-b31e-18db418f0f09" />
</p>

<p align="center">
  <img width="1456" height="921" alt="Task Manager Screenshot 2" src="https://github.com/user-attachments/assets/11168c56-54d5-4b0f-ab23-a8262cd962f0" />
</p>

---

## 🚀 Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ashishpant31/Task_Management_System.git
   cd Task_Management_System
   ```

2. **Create & Activate a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   ```
   - **Windows:** `.\venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install at least: `streamlit`)*

4. **Run the App**
   ```bash
   streamlit run app.py
   ```
   The dashboard will open in your default browser.

---

## 💡 Usage

- Add new tasks using the sidebar form.
- Click on an active task’s header to edit its details.
- Mark tasks as completed with the ✔️ button.
- Reopen completed tasks with the ↩️ button.
- Active tasks are auto-ranked, and completed tasks archived separately.
- Export task data to CSV using the built-in export function.

---

## 📋 Data & Privacy

- All task data is stored locally in an SQLite database (`tasks.db`).
- No data is sent externally.
- CSV export is optional and can be enabled or disabled.

---

## 🤝 Contributing

Contributions are welcome!  
Fork the repository and open a pull request with your improvements or bug fixes.

---

## 📝 License

This project is licensed under the MIT License.

---

## 📬 Contact

For questions or feedback, please open an issue on the GitHub repository.

---

## 📂 Notes on `.gitignore`

To keep the repo clean, make sure to include the following in your `.gitignore`:

```
venv/
*.pyc
__pycache__/
.DS_Store
*.csv
tasks.db
```

---

Thank you for checking out the Task Management System!  
Built with ❤️ and [Streamlit](https://streamlit.io).
