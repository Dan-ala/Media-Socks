from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(15))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash,password)


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)

class SocksCategory(db.Model):
    __tablename__ = "socks_category"
    id = db.Column(db.Integer, primary_key=True)
    socks_category_name = db.Column(db.String(50), nullable=False)

class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    socks_category_id = db.Column(db.Integer, db.ForeignKey('socks_category.id'), nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    product_image = db.Column(db.String(100))
    recycle_bin = db.Column(db.Boolean, default=False)

class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    total_price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
