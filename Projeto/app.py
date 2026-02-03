from flask import Flask, render_template
from database import computadores

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", pcs=computadores)

if __name__ == "__main__":
    app.run(debug=True)
