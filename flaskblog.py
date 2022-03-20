from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h>Home</h>"

@app.route("/about")
def about():
    return "<p>About page</p>"


if __name__ == '__main__' :
    app.run(debug=True)


