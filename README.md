# To-Do List Web Application

A simple and responsive To-Do List web application built using **Python Flask**, **HTML**, **CSS**, and **Bootstrap**.

This project allows users to manage their daily tasks by adding, updating, deleting, and marking tasks as completed.

## Features

* Add new tasks with a title and description
* View all added tasks
* Update existing tasks
* Delete tasks
* Mark tasks as completed
* Display task status
* Display task creation time
* Responsive design for smaller screens
* Bootstrap-based user interface
* Custom CSS styling

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* Bootstrap 5
* Jinja2

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
├── index1.html
├── .gitignore
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Shubham07jee/To-Do-List-ShubhamC.git
```

### 2. Open the project directory

```bash
cd DEVCORE_TO_DO_LIST
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

On Linux/Ubuntu:

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

## How It Works

The application uses Flask routes to perform different task operations:

* `/` → Add and display tasks
* `/update/<sno>` → Update a task
* `/delete/<sno>` → Delete a task
* `/mark/<sno>` → Mark a task as completed

Tasks are currently stored in memory while the Flask application is running.

## Future Improvements

Some possible improvements for the future are:

* Add database storage
* Add user authentication
* Add task categories
* Add due dates
* Add task filtering and searching
* Improve task validation

## Author

**Shubham Chaudhari**

This project was created as part of the **DevCore learning/project task**.
