from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='48723eba0dbb70e122a0b44899278b46'
posts=[
    {
        'Author':'Victor',
        'Content':'Call of the World',
        'Date_posted':'18/12/2003'

    },
    {
        'Author':'Peter',
        'Content':'Hello World',
        'Date_posted':'07/03/2023'

    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')


@app.route("/register")
def register():
    form=RegistrationForm()
    return render_template('register.html',title='Register', form= form)

@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',title='Login', form= form)
app.run(debug=True)