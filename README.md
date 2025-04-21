# Tu Duu - Todo Application

**Tu Duu** is a simple and user-friendly todo list application built with **Django**,
where you can manage your tasks efficiently. You can add, edit, delete tasks,
and filter or sort them by priority and status.

---

## Features

- **Task Management**: Add, edit, and delete tasks.
- **Task Status**: Filter tasks by status (To-Do, In Progress, Done).
- **Priority Management**: Filter tasks by priority (High, Medium, Low).
- **Sorting**: Sort tasks by creation date or priority.
- **User Authentication**: Sign up and login to manage your tasks securely.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jobdaiyoung/Todo-Application.git
cd Todo-Application
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- For Windows:
```bash
venv\Scripts\activate
```
- For macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5.Set Up Database
```bash
cd todo_project
python manage.py migrate
```

### 6.Create a Superuser (optional, for admin access)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser to access the app.
