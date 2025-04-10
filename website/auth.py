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

        user = User.query.filter_by(username=username).first()
        user_email = User.query.filter_by(email=email).first()

        if user:
            flash('Username already exists.', category='danger')
        elif user_email:
            flash('Email address already in use.', category='danger')
        elif len(username) < 5:
            flash('Username is too short.', category='danger')
        elif len(password) < 7:
            flash('Password must be at least 7 characters long.', category='danger')
        elif password != conf_password:
            flash('Passwords do not match.', category='danger')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password))
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