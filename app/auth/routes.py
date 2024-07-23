from flask import flash, render_template, request, session, redirect, url_for
import app

from flask_login import login_user, logout_user, login_manager

from flask import Blueprint

from app import models
from app.adapter import CustomerUserAdapter
auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

# @login_manager.user_loader
# def load_user(customer_id):
#     customer = models.Customer.query.get(int(customer_id))
#     if customer:
#         return CustomerUserAdapter(customer)
#     return None


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        e = request.form.get('email')
        p = request.form.get('password_hash')

        print(f"Data: {e, p}")

        user = models.Customer.query.filter_by(email=e).first()
        if user and user.check_password(p):
            login_user(CustomerUserAdapter(user))
            return redirect(url_for('products.products_list'))
        else:
            flash('Invalid credentials, please try again.')
            return redirect(url_for('auth.login'))
    return render_template("login.html", N=1)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        u = request.form.get('username')
        p = request.form.get('password_hash')
        e = request.form.get('email')
        p_n = request.form.get('phone_number')

        print(f"Registered Data: {u, p, e, p_n}")

        user = app.models.Customer.query.filter_by(username=u).first()
        if user:
            print("User already here")
            return render_template("login.html", N=2)
        else:
            new_customer = app.models.Customer(
                username=u,
                email=e,
                phone_number=p_n
            )
            new_customer.set_password(p)

            app.db.session.add(new_customer)
            app.db.session.commit()
            session['username'] = u
            return redirect(url_for('products.products_list'))
    return render_template("login.html", N=2)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))