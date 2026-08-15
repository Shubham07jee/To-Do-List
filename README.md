# To-Do List Web Application

A simple To-Do List web application built using **Python Flask**, **HTML**, **CSS**, **Bootstrap**, and **SQLite**.

The application allows users to create, view, update, delete, and mark tasks as completed. SQLite is used as the local database for storing task information.

## Features

- Add new tasks with a title and description
- View all tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- Display task status
- Display task creation time
- Store task data using SQLite
- Responsive user interface
- Bootstrap-based styling
- Custom CSS styling

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Jinja2

## Project Structure

```text
DEVCORE_TO_DO_LIST/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── update.html
│
├── app.py
├── database.py
├── .gitignore
└── README.md
````

## Database

This project uses **SQLite** as its database.

The local database file is:

```text
todos.db
```

The database contains the following tables:

* `todos`
* `users`

### `todos` Table

| Column         | Data Type | Constraint                |
| -------------- | --------- | ------------------------- |
| `sno`          | INTEGER   | PRIMARY KEY AUTOINCREMENT |
| `title`        | TEXT      | NOT NULL                  |
| `desc`         | TEXT      | NOT NULL                  |
| `date_created` | DATETIME  | —                         |
| `status`       | TEXT      | —                         |

The application performs the following database operations:

* **Create** – Add a new task
* **Read** – Display existing tasks
* **Update** – Modify task information or status
* **Delete** – Remove a task

## Application Flow

```text
User
  ↓
HTML / Bootstrap Interface
  ↓
Flask Application
  ↓
Database Functions
  ↓
SQLite Database
```

The Flask application handles task operations such as:

* Adding tasks
* Displaying tasks
* Updating tasks
* Deleting tasks
* Marking tasks as completed

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Shubham07jee/To-Do-List-ShubhamC.git
```

### 2. Enter the project directory

```bash
cd To-Do-List-ShubhamC
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

On Ubuntu/Linux:

```bash
source venv/bin/activate
```

### 5. Install Flask

```bash
pip install flask
```

### 6. Run the application

```bash
python app.py
```

### 7. Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Git and Database Files

The SQLite database is used locally by the application.

The following files are intentionally ignored by Git:

```text
*.db
*.db-journal
*.sqbpro
```

This prevents local database files and SQLite Browser project files from being uploaded to the repository.

When the application runs on another computer, the SQLite database can be created locally by the application.

## Future Improvements

Possible future improvements include:

* User authentication
* Task categories
* Due dates
* Task priorities
* Task searching and filtering
* Improved input validation
* User-specific task management
* Online deployment

## Author

**Shubham Chaudhari**

Developed as part of a **DevCore learning/project task**.

````

### One thing I would NOT do

Don't put the actual binary contents of `todos.db` into the README. What you showed earlier:

```text
SQLite format 3...
````

is the **binary SQLite database**, not something that belongs in a README.

Your current setup is actually good:

```text
todos.db       → local database
*.db           → ignored by Git
*.sqbpro       → ignored by Git
database.py    → database logic tracked by Git
README.md      → documentation tracked by Git
```


