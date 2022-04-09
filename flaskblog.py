import sys
sys.path.insert(1, '/users/podda/anaconda3/lib/site-packages')
from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm , LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '952525frbgrrgirg'

posts = [

    {
        'author' : 'Harsh',
        'title'  : 'Blog post 1',
        'content': ' First post content',
        'date_posted' : ' 1st May 2022'

    }


]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for{form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form = form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in!", 'success')
            return redirect (url_for('home'))
        else:
            flash("login failed. Please check username and password",'danger')
    return render_template('login.html',title='Login',form = form)

if __name__ == '__main__' :
    app.run(debug=True)


