# 📈 Task Management System

## 📖 About

**Task Management System** is a simple, intuitive web app built with [Streamlit](https://streamlit.io) and SQLite. It enables personal and team task management with the ability to create, edit, prioritize, and track task completion easily through a clean interface.

---

## ✨ Features

- Add, edit, and update tasks with details including title, description, priority, status, and optional deadlines.
- Active and completed tasks are displayed separately with clear UI.
- Editable tasks on clicking active tasks; read-only view for completed tasks.
- Automatic ranking of active tasks based on priority and deadline.
- Persistent storage using SQLite database.
- Optional exporting of task data to CSV for offline review.
- Responsive and minimal UI powered by Streamlit's rapid app development features.

---

## 🖼️ Screenshots

### Task Management UI - Active and Completed tasks
<p align="center">
  <img width="1493" height="728" alt="Task Manager Screenshot 1" src="https://github.com/user-attachments/assets/ab750486-c96b-4b42-b31e-18db418f0f09" />
</p>

<p align="center">
  <img width="1456" height="921" alt="Task Manager Screenshot 2" src="https://github.com/user-attachments/assets/11168c56-54d5-4b0f-ab23-a8262cd962f0" />
</p>

---

## 🚀 Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ashishpant31/Task_Management_System.git
   cd Task_Management_System
   ```


2. **Create and activate a Virtual Environment (recommended):**
   ```bash
   python -m venv venv
   ```
   - **Windows:** `.\venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`

  
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If requirements.txt is missing, install: streamlit)*

4. **Run the app:**
```bash
   streamlit run app.py
   ```
   The dashboard will open in your default web browser.
  
---

## 💡 Usage

- Add new tasks via the sidebar form.
- Click active task headers to edit details.
- Mark tasks completed with the ✔️ button.
- Reopen completed tasks with the ↩️ button.
- Tasks are auto-ranked, and completed tasks are archived separately.
- Export your task data to CSV (optional, built-in function available).

---

## 📋 Data & Privacy

- All data is stored locally in an SQLite database (`tasks.db`).
- No data is sent externally.
- CSV export function is optional and can be enabled/disabled.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and open a pull request with improvements or bug fixes.

---

## License

This project is licensed under the MIT License.

---

## Contact

For any questions or feedback, please open an issue on the GitHub repository.

---

## Notes on `.gitignore`

To keep the repo clean and prevent unnecessary files, make sure to ignore:
```bash
venv/
*.pyc
pycache/
.DS_Store
*.csv
tasks.db
```
---

Thank you for checking out the Task Management System!  
Built with ❤️ and [Streamlit](https://streamlit.io).
