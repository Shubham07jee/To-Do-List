from flask import Flask , render_template  # first flask is library and second is class

app = Flask(__name__)

todo = [
    {"Sr no" : 1, "title":"Sample Task",
    "Desc":"This is a sample task for to do list","Status":"Pending"}
]

@app.route("/")
def home():
    return render_template("index.html")  #After this writing we have import the render_template at top

if __name__ == "__main__":
    app.run(debug=True)