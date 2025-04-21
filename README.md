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

## Framework
This project is built using **Django**, a high-level Python web framework that promotes rapid development and clean, pragmatic design.

I used:
- Django views and templates for rendering frontend pages.
- Django's built-in authentication system (customized manually) for user login and signup.
- Bootstrap 5 for responsive styling and a clean UI.

---

## Database

The application uses **SQLite3** by default, which is Django’s default lightweight relational database.

### Database Structure:

- **User** (Django's built-in User model)
- **Todo**
  - `id` (AutoField, Primary Key)
  - `title` (CharField)
  - `description` (TextField)
  - `status` (CharField – "To Do", "In Progress", "Done")
  - `created_at` (DateTimeField – auto_now_add)
  - `user` (ForeignKey to Django User model)
  - `priority` (CharField – "Low", "Medium", "High")

---

## Application Deployment

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

---

## Code Explanation
#### System Architecture Diagram (Layered Architecture)

![Architecture Diagram](todo_project/todos/static/Architecture%20Diagram.png)
1. Presentation Layer (Frontend/UI)
- Handles user interaction via HTML templates styled with Bootstrap.
- Contains reusable UI components like:
  - `base.html` → Layout, navbar, and Bootstrap integration
  - `login.html`, `signup.html`, `todo_list.html`, etc.
- Displays data and receives input from users.

2. Business Logic Layer
- Found in `views.py` and `forms.py`.
- Responsible for:
  - Handling user authentication (login, logout, signup)
  - Processing form submissions (add/update/delete todos)
  - Fetching filtered data (e.g., todos specific to the logged-in user)
- Connects the UI with the database and applies app rules (like access control).

3. Data Access Layer (Models)
- Contains:
  - Todo model linked to Django’s built-in User model.
- Interacts with the underlying database (SQLite or PostgreSQL) using Django ORM.
