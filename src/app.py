from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to my webiste"

@app.route("/about"):
def about():
    return("My name is A.J")


if __name__ == "__main__":
    app.run()


