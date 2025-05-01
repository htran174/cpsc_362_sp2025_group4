import os

from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from flask_login import current_user, login_required, logout_user
from werkzeug.utils import secure_filename

from . import db
from .models import CartItem
from .products import products

checkout = Blueprint('checkout', __name__)

@checkout.route('/cart')
@login_required
def cart():
    cart = CartItem.query.filter_by(user_id=current_user.id).all()
    cart_items = []
    subtotal = 0

    for product in cart:
        quantity = product.quantity
        product_object = next((p for p in products if p['id'] == product.legacy_id), None)
        for _ in range(quantity):
            if product_object:
                cart_items.append(product_object)
                subtotal += product_object['price']

    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal, user=current_user)

@checkout.route('/add_to_cart', methods=['POST'])
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

@checkout.route('/remove_from_cart', methods=['POST'])
@login_required
def remove_from_cart():
    product_id = int(request.form.get('product_id'))

    cart_item = CartItem.query.filter_by(legacy_id=product_id, user_id=current_user.id).first()
    cart_item.quantity -= 1
    if cart_item.quantity <= 0:
        db.session.delete(cart_item)
    db.session.commit()

    return redirect(url_for('checkout.cart'))

@checkout.route('/checkout')
@login_required
def fcheckout():
    cart = CartItem.query.filter_by(user_id=current_user.id).all()
    cart_items = []
    subtotal = 0

    for product in cart:
        product_object = next((p for p in products if p['id'] == product.legacy_id), None)
        if product_object:
            cart_items.append(product_object)
            subtotal += product_object['price']

    return render_template('checkout.html', cart_items=cart_items, subtotal=subtotal, user=current_user)

@checkout.route('/place_order', methods=['POST'])
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