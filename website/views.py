from flask import Blueprint, render_template, request, redirect, session, url_for
from flask_login import current_user, login_required, logout_user

from .products import products
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/shirts')
def shirts():
    return render_template('shirts.html', user=current_user)

@views.route('/watches')
def watches():
    return render_template('watches.html', user=current_user)

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
    return render_template('product.html', product=product, user=current_user)


@views.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    if not product_id:
        return redirect(request.referrer)  # Go back to the same page

    cart = session.get('cart', [])
    cart.append(int(product_id))
    session['cart'] = cart

    return redirect(request.referrer)

@views.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = int(request.form.get('product_id'))

    cart = session.get('cart', [])

    if product_id in cart:
        cart.remove(product_id)
        session['cart'] = cart

    return redirect(url_for('views.cart'))

@views.route('/checkout')
def checkout():
    cart = session.get('cart', [])
    cart_items = []
    subtotal = 0

    for product_id in cart:
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            cart_items.append(product)
            subtotal += product['price']

    return render_template('checkout.html', cart_items=cart_items, subtotal=subtotal, user=current_user)

@views.route('/place_order', methods=['POST'])
def place_order():
    name = request.form.get('name')
    address = request.form.get('address')
    email = request.form.get('email')
    payment = request.form.get('payment')

    # After order placed, clear the cart
    session['cart'] = []

    # You can pass name or whatever to thank you page if you want
    return render_template('order_confirmation.html', name=name, user=current_user)

# TO DO: ALLOW USER TO UPLOAD PICTURES OF PRODUCT
@views.route('/create-product', methods=['POST', 'GET'])
def create_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        category = request.form.get('category')
        subcategory = request.form.get('subcategory')
        variant = request.form.get('variant')
        is_default_variant = request.form.get('is_default_variant')
        is_variant_of = request.form.get('is_variant_of')

        if is_default_variant == 'on':
            is_default_variant = True
        else:
            is_default_variant = False

        default_variant_id = None
        if is_variant_of:
            default_variant_id = Product.query.filter_by(name=is_variant_of).first().id

        product = Product(name=name, price=price, quantity=quantity, category=category, subcategory=subcategory, variant=variant, is_default_variant=is_default_variant, default_variant_id=default_variant_id)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('views.home'))

    return render_template('create-product.html')