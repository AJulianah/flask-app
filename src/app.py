from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to my webiste"

@app.route("/about")
def about():
    return "My name is A.J"

@app.route("/contact")
def contact():
    return "Email: test@gmail.com"

@app.route("/article")
def article:
    return "This is my first article"


if __name__ == "__main__":
    app.run()


