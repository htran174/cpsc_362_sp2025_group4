import os

from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from flask_login import current_user, login_required, logout_user
from werkzeug.utils import secure_filename

from . import db
from .models import CartItem
from .products import products

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/shirts')
def shirts():
    return render_template('shirts.html', user=current_user)

@views.route('/mpants')
def mpants():
    return render_template('mpants.html', user=current_user)

@views.route('/jackets')
def jackets():
    return render_template('jackets.html', user=current_user)

@views.route('/dresses')
def dresses():
    return render_template('dresses.html', user=current_user)

@views.route('/tops')
def tops():
    return render_template('tops.html', user=current_user)

@views.route('/wpants')
def wpants():
    return render_template('wpants.html', user=current_user)

@views.route('/watches')
def watches():
    return render_template('watches.html', user=current_user)

@views.route('/rings')
def rings():
    return render_template('rings.html', user=current_user)

@views.route('/necklaces')
def necklaces():
    return render_template('necklaces.html', user=current_user)

@views.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404

    from_page = request.args.get("from_page", "/")  # default to home
    return render_template('product.html', product=product, from_page=from_page, user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template('profile/summary.html', user=current_user, current_tab='summary')

@views.route('/profile/settings')
@login_required
def profile_settings():
    return render_template('profile/settings.html', user=current_user, current_tab='settings')

@views.route('/profile/orders')
@login_required
def profile_orders():
    return render_template('profile/orders.html', user=current_user, current_tab='orders')

@views.route('/catalog')
def catalog():
    return render_template('catalog.html', products=products, user=current_user)