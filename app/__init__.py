from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.adapter import CustomerUserAdapter

from .config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # LoginManager configuration
    login_manager.session_protection = "strong"
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    @login_manager.user_loader
    def load_user(customer_id):
        customer = models.Customer.query.get(int(customer_id))
        if customer:
            return CustomerUserAdapter(customer)
        return None

    # Register blueprints
    from .auth.routes import auth
    from .products.routes import products
    app.register_blueprint(auth)
    app.register_blueprint(products)

    # Import models
    from .models import Category, Customer, Order, SocksCategory, Product

    return app
