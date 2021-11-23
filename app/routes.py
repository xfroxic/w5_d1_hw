# routes are different URLs that the application will import

from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')


@app.route('/index')
def index():
    user = {'username':'Frank'}
    posts = [
        {
            'author':{'username':'Frank'},
            'body':'Cold day in Illinois'
        },
        {
            'author':{'username':'Amber'},
            'body':'I hate action movies...'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')