from flask import Blueprint, render_template, flash, redirect, url_for, request, get_flashed_messages
from flask_login import current_user, login_user, logout_user, login_required
from app.auth_forms import LoginForm, RegistrationForm
from app.models import User
from app.extensiones import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
   return render_template('home.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # return f'JAJAJ{current_user.username}'
        return render_template('dashboard.html')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        #return render_template('index.html')
        return render_template('dashboard.html')
    return render_template('login.html', title='Sign In', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
  

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)



