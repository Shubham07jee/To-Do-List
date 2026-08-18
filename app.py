from flask import Flask, render_template, request, redirect
from database import (
    init_db,
    add_todo,
    get_all_todos,
    get_todo,
    update_todo,
    delete_todo,
    mark_completed
)

app = Flask(__name__)

init_db()


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        add_todo(title, desc)

        return redirect("/")

    allTodo = get_all_todos()

    return render_template("index.html", allTodo=allTodo)


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):

    todo = get_todo(sno)

    if todo is None:
        return "Task Not Found"

    if request.method == "POST":

        title = request.form["title"]
        desc = request.form["desc"]

        update_todo(sno, title, desc)

        return redirect("/")

    return render_template("update.html", todo=todo)


@app.route('/delete/<int:sno>')
def delete(sno):

    delete_todo(sno)

    return redirect("/")


@app.route('/mark/<int:sno>')
def mark(sno):

    mark_completed(sno)

    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)