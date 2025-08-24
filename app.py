import streamlit as st
import sqlite3
from datetime import datetime, date


DB_FILE = "tasks.db"


# Initialize the SQLite database and create the tasks table if it doesn't exist
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            priority TEXT NOT NULL,
            deadline TEXT
        )
    ''')
    conn.commit()
    conn.close()


# Retrieve active tasks (not completed) from the database and rank them by priority and deadline
def get_tasks():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM tasks WHERE status != "Completed"')
    rows = c.fetchall()
    conn.close()
    def rank(task):
        priority_score = {'High': 3, 'Medium': 2, 'Low': 1}.get(task['priority'], 0)
        deadline_val = task['deadline']
        if deadline_val:
            try:
                deadline_dt = datetime.fromisoformat(deadline_val)
                deadline_score = max(0, (deadline_dt - datetime.now()).days)
            except Exception:
                deadline_score = 1000
        else:
            deadline_score = 1000
        return priority_score * 100 - deadline_score
    tasks = [dict(zip(['id', 'title', 'description', 'status', 'priority', 'deadline'], r)) for r in rows]
    tasks.sort(key=rank, reverse=True)
    return tasks


# Retrieve completed tasks from the database
def get_completed_tasks():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM tasks WHERE status = "Completed"')
    rows = c.fetchall()
    conn.close()
    return [dict(zip(['id', 'title', 'description', 'status', 'priority', 'deadline'], r)) for r in rows]


# Add a new task to the database with provided details
def add_task(title, desc, status, priority, deadline):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('INSERT INTO tasks (title, description, status, priority, deadline) VALUES (?,?,?,?,?)',
              (title, desc, status, priority, deadline if deadline else ""))
    conn.commit()
    conn.close()


# Update an existing task's details in the database
def update_task(task_id, title, desc, status, priority, deadline):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('UPDATE tasks SET title=?, description=?, status=?, priority=?, deadline=? WHERE id=?',
              (title, desc, status, priority, deadline if deadline else "", task_id))
    conn.commit()
    conn.close()


# Change the status of a task (e.g., mark as Completed or Pending)
def update_status(task_id, new_status):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('UPDATE tasks SET status=? WHERE id=?', (new_status, task_id))
    conn.commit()
    conn.close()


# Delete a task from the database by its ID
def delete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()
    conn.close()


# Remove all tasks from the database (used when clearing all tasks)
def clear_all_tasks():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('DELETE FROM tasks')
    conn.commit()
    conn.close()


# Return a colored badge emoji string based on task priority
def priority_badge(priority):
    colors = {
        "High": "🔴 High",
        "Medium": "🟠 Medium",
        "Low": "🟢 Low"
    }
    return colors.get(priority, priority)


# Return a colored badge emoji string based on task status
def status_badge(status):
    colors = {
        "Pending": "🟡 Pending",
        "In-Progress": "🔵 In-Progress",
        "Completed": "🟢 Completed"
    }
    return colors.get(status, status)


# Initialize the database at app start
init_db()


st.title("📝 Task Manager")

# Initialize session state dictionaries for toggling task details visibility
if "show_active" not in st.session_state:
    st.session_state.show_active = {}

if "show_completed" not in st.session_state:
    st.session_state.show_completed = {}

# Button to clear all tasks and reset visibility states
if st.button("🗑️ Clear All Tasks"):
    clear_all_tasks()
    st.session_state.show_active = {}
    st.session_state.show_completed = {}
    st.warning("All tasks deleted.")

# Toggle visibility of active task details
def toggle_active(task_id):
    st.session_state.show_active[task_id] = not st.session_state.show_active.get(task_id, False)

# Toggle visibility of completed task details
def toggle_completed(task_id):
    st.session_state.show_completed[task_id] = not st.session_state.show_completed.get(task_id, False)

# Display active tasks with editable details on click
st.header("Active Tasks (auto-ranked)")
tasks = get_tasks()

if not tasks:
    st.info("No active tasks found.")
else:
    for task in tasks:
        task_id = task['id']
        cols = st.columns([0.5, 8])
        if cols[0].button('✔️', key=f"complete_{task_id}"):
            update_status(task_id, "Completed")
            st.rerun()

        title_str = f"{task['title']} (Priority: {priority_badge(task['priority'])}, Status: {status_badge(task['status'])}, Deadline: {task['deadline']})"
        if cols[1].button(title_str, key=f"title_{task_id}"):
            toggle_active(task_id)

        if st.session_state.show_active.get(task_id, False):
            with st.form(f"edit_form_{task_id}"):
                new_title = st.text_input("Title", value=task['title'], key=f"edit_title_{task_id}")
                new_desc = st.text_area("Description", value=task['description'], key=f"edit_desc_{task_id}")
                new_status = st.selectbox("Status", ["Pending", "In-Progress", "Completed"], index=["Pending", "In-Progress", "Completed"].index(task['status']), key=f"edit_status_{task_id}")
                new_priority = st.selectbox("Priority", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(task['priority']), key=f"edit_priority_{task_id}")
                new_deadline = st.date_input("Deadline", value=date.fromisoformat(task['deadline']) if task['deadline'] else None, key=f"edit_deadline_{task_id}")
                update_btn = st.form_submit_button("Update Task")
                if update_btn and new_title.strip():
                    update_task(task_id, new_title.strip(), new_desc.strip(), new_status, new_priority,
                                new_deadline.isoformat() if new_deadline else "")
                    st.success("Task updated. Please refresh.")

# Visual separator
st.markdown("<hr style='border:2px solid #4CAF50'>", unsafe_allow_html=True)

# Display completed tasks with read-only description on click
st.header("Completed Tasks")
done_tasks = get_completed_tasks()

if not done_tasks:
    st.info("No completed tasks yet.")
else:
    for task in done_tasks:
        task_id = task['id']
        cols = st.columns([0.5, 8])
        if cols[0].button('↩️', key=f"reopen_{task_id}"):
            update_status(task_id, "Pending")
            st.rerun()

        title_str = f"✅ {task['title']} (Completed), Priority: {priority_badge(task['priority'])}, Deadline: {task['deadline']}"
        if cols[1].button(title_str, key=f"c_title_{task_id}"):
            toggle_completed(task_id)

        if st.session_state.show_completed.get(task_id, False):
            st.markdown(f"**Description:**\n{task['description'] or 'No description'}")

# Sidebar form to add new tasks with input clearing on submit
st.sidebar.header("Add New Task")
with st.sidebar.form("add_task_form", clear_on_submit=True):
    title = st.text_input("Title", key="title")
    description = st.text_area("Description", key="description")
    status = st.selectbox("Status", ["Pending", "In-Progress", "Completed"], key="status")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"], key="priority")
    deadline = st.date_input("Deadline (optional)", value=None, min_value=date.today(), key="deadline")

    submitted = st.form_submit_button("✅ Add Task")
    if submitted and title.strip():
        add_task(title.strip(), description.strip(), status, priority, deadline.isoformat() if deadline else "")
        st.success(f"Task '{title}' added!")
        try:
            st.rerun()
        except AttributeError:
            st.info("Please refresh the page to see the updated task list.")


