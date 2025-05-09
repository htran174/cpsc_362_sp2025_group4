import functools
from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='danger')
        else:
            flash('Username does not exist, try again.', category='danger')

    return render_template("sign-in.html")

@auth.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        conf_password = request.form.get('conf_password')
        full_name = request.form.get('fullname')
        birthday = request.form.get('birthday')
        birthday_date = datetime.strptime(birthday, '%Y-%m-%d').date()
        user = User.query.filter_by(username=username).first()
        user_email = User.query.filter_by(email=email).first()

        special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

        if user:
            flash('Username already exists.', category='danger')
        elif user_email:
            flash('Email address already in use.', category='danger')
        elif len(username) < 4:
            flash('Username is too short.', category='danger')
        elif any((not char.isalnum() and char != '_') for char in username):
            flash('Username contains invalid characters.', category='danger')
        elif len(password) < 8:
            flash('Password must be at least 8 characters long.', category='danger')
        elif not any(char.isupper() for char in password):
            flash('Password must contain an uppercase character.', category='danger')
        elif not any(char.isdigit() for char in password):
            flash('Password must contain a number.', category='danger')
        elif not any(char in special_characters for char in password):
            flash('Password must contain a special character.', category='danger')
        elif password != conf_password:
            flash('Passwords do not match.', category='danger')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password), full_name=full_name, birthday=birthday_date)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("sign-up.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/profile')
@login_required
def profile():
    return render_template('profile/summary.html', user=current_user, current_tab='summary')

@auth.route('/profile/settings', methods=['POST','GET'])
@login_required
def profile_settings():
    return render_template('profile/settings.html', user=current_user, current_tab='settings')

@auth.route('/profile/settings/edit', methods=['POST','GET'])
@login_required
def profile_settings_edit():
    success_editing = False

    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    conf_password = request.form.get('conf_password')

    if email:
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email address already in use.', category='danger')
        else:
            success_editing = True
            current_user.email = email
    if username:
        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            flash('Username already in use.', category='danger')
        elif len(username) < 4:
            flash('Username is too short.', category='danger')
        elif any((not char.isalnum() and char != '_') for char in username):
            flash('Username contains invalid characters.', category='danger')
        else:
            success_editing = True
            current_user.username = username
    if password:
        special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        if len(password) < 8:
            flash('Password must be at least 8 characters long.', category='danger')
        elif not any(char.isupper() for char in password):
            flash('Password must contain an uppercase character.', category='danger')
        elif not any(char.isdigit() for char in password):
            flash('Password must contain a number.', category='danger')
        elif not any(char in special_characters for char in password):
            flash('Password must contain a special character.', category='danger')
        elif password != conf_password:
            flash('Passwords do not match.', category='danger')
        else:
            success_editing = True
            current_user.password = generate_password_hash(password)
    db.session.commit()
    if success_editing:
        flash('Account edits successful.', category='success')

    return redirect(request.referrer)

@auth.route('/profile/orders')
@login_required
def profile_orders():
    return render_template('profile/orders.html', user=current_user, current_tab='orders')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if current_user.is_authenticated:
            return view(*args, **kwargs)
        else:
            flash('You must be logged in to view this page.', category='danger')
            return redirect(url_for('auth.login'))
    return wrapped_view