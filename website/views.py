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

@views.route('/cart')
def cart():
    cart = session.get('cart', [])
    cart_items = []
    subtotal = 0

    for product_id in cart:
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            cart_items.append(product)
            subtotal += product['price']

    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal, user=current_user)

@views.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404

    from_page = request.args.get("from_page", "/")  # default to home
    return render_template('product.html', product=product, from_page=from_page, user=current_user)

@views.route('/cart')
@login_required
def cart():
    cart = CartItem.query.filter_by(user_id=current_user.id).all()
    cart_items = []
    subtotal = 0

    for product in cart:
        product_object = next((p for p in products if p['id'] == product.legacy_id), None)
        if product_object:
            cart_items.append(product_object)
            subtotal += product_object['price']

    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal, user=current_user)

@views.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    product_id = request.form.get('product_id')
    if not product_id:
        return redirect(request.referrer)  # Go back to the same page

    existing_item = CartItem.query.filter_by(legacy_id=product_id, user_id=current_user.id).first()
    if existing_item:
        existing_item.quantity += 1
        db.session.commit()
        flash('Added to cart.', category='success')
        return redirect(request.referrer)

    cart_item = CartItem(legacy_id=product_id, quantity=1, user_id=current_user.id)
    db.session.add(cart_item)
    db.session.commit()
    flash('Added to cart.', category='success')

    return redirect(request.referrer)

@views.route('/remove_from_cart', methods=['POST'])
@login_required
def remove_from_cart():
    product_id = int(request.form.get('product_id'))

    cart_item = CartItem.query.filter_by(legacy_id=product_id, user_id=current_user.id).first()
    db.session.delete(cart_item)
    db.session.commit()

    return redirect(url_for('views.cart'))

@views.route('/checkout')
@login_required
def checkout():
    cart = CartItem.query.filter_by(user_id=current_user.id).all()
    cart_items = []
    subtotal = 0

    for product in cart:
        product_object = next((p for p in products if p['id'] == product.legacy_id), None)
        if product_object:
            cart_items.append(product_object)
            subtotal += product_object['price']

    return render_template('checkout.html', cart_items=cart_items, subtotal=subtotal, user=current_user)

@views.route('/place_order', methods=['POST'])
@login_required
def place_order():
    name = request.form.get('name')
    address = request.form.get('address')
    email = request.form.get('email')
    payment = request.form.get('payment')

    # After order placed, clear the cart
    cart = CartItem.query.filter_by(user_id=current_user.id).all()
    for product in cart:
        db.session.delete(product)
    db.session.commit()

    # You can pass name or whatever to thank you page if you want
    return render_template('order_confirmation.html', name=name, user=current_user)
