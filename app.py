from flask import Flask , render_template  # first flask is library and second is class

app = Flask(__name__)

todo = [
    {"Sr no" : 1, "title":"Sample Task",
    "desc":"This is a sample task for to do list","date_created":"08-08-2026","Status":"Pending", "Action":""}
]

@app.route("/")
def home():
    return render_template("index.html",allTodos = todo)  #After this writing we have import the render_template at top

if __name__ == "__main__":
    app.run(debug=True)