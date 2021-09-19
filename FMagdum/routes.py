from flask import render_template,url_for, flash, redirect
from FMagdum import app, db, bcrypt
from FMagdum.forms import RegistrationForm, LoginForm
from FMagdum.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Faisal Magdum',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Sept 13, 2021'
    },
    {
        'author': 'Sana Magdum',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Sept 14, 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode()
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in','Success')
            return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check email and password','danger')
        return render_template('login.html', title='Login', form=form)

@app.route("/logout", methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
