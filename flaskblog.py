from flask import Flask, render_template,url_for
from matplotlib.pyplot import title

app = Flask(__name__)



posts = [

    {
        'author' : 'harsh',
        'title'  : 'Blog post 1',
        'content': ' First post content',
        'date_posted' : ' 1st may 2022'

    }


]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')


if __name__ == '__main__' :
    app.run(debug=True)


