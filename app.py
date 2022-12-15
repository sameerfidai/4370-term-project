from flask import Flask, render_template
import conLayer

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/db")
def db():
    data = conLayer.dbConnection()
    return "connected to database"


if __name__ == "__main__":
    app.run(debug=True)
