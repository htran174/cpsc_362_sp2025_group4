from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    payments = db.relationship('Payment', backref='user', lazy=True)
    full_name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.Date, nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    subcategory = db.Column(db.String(80), nullable=False)
    image_dir = db.Column(db.String(320), nullable=False)
    thumbnail_dir = db.Column(db.String(320), nullable=False)

    def validate_nonnegative_stock(self):
        if self.stock < 0:
            raise ValueError('Stock cannot be negative')
        return True

class ProductVariant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variant_name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_dir = db.Column(db.String(320), nullable=False)
    thumbnail_dir = db.Column(db.String(320), nullable=False)

    base_product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def validate_nonnegative_stock(self):
        if self.stock < 0:
            raise ValueError('Stock cannot be negative')
        return True

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    legacy_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    variant_id = db.Column(db.Integer, db.ForeignKey('product_variant.id'))

    def validate_product_id(self):
        if not self.product_id and not self.legacy_id and not self.variant_id:
            raise ValueError('One product ID type required')
        return True
