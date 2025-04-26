from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    payments = db.relationship('Payment', backref='user', lazy=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    default_variant_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    subcategory = db.Column(db.String(80), nullable=False)
    variant = db.Column(db.String(80), nullable=False)
    is_default_variant = db.Column(db.Boolean, nullable=False)
    is_variant_of = db.Relationship('Product', remote_side=[id], lazy=True)

    def validate_variants(self):
        if self.is_variant_of & self.is_default_variant:
            raise ValueError('Something is a default variant and a variant of something')
        return True