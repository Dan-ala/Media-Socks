import os
from flask import Blueprint, redirect, render_template, request, send_from_directory, url_for
from flask_login import current_user, login_required
from app import models, db

products = Blueprint('products', __name__, url_prefix='/products', 
                     template_folder='templates')

@products.route("/")
def products_list():
    user = current_user
    prods = []
    u = []
    if user.is_authenticated:
        print("User is authenticated")

        prods = models.Product.query.all()
        u = models.Customer.query.all()

    return render_template("products.html", prods=prods, u=u)


@products.route("/new", methods=["GET", "POST"])
@login_required
def new_products():
    categories = models.Category.query.all()
    socks_categories = models.SocksCategory.query.all()

    if request.method == "POST":
        category_id = request.form.get("category_id")
        socks_category_id = request.form.get("socks_category_id")
        product_name = request.form.get("product_name")
        quantity = request.form.get("quantity")
        price = request.form.get("price")
        product_image = request.files["product_image"]

        print (f"Data inserted: {category_id, socks_category_id, product_name, quantity, price, product_image}")

        # Save the uploaded file
        filename = product_image.filename
        file_path = os.path.join(os.path.abspath(os.getcwd()), 'app', 'products', 'img', filename)
        product_image.save(file_path)

        # Create and add the new product
        new_product = models.Product(
            category_id=category_id,
            socks_category_id=socks_category_id,
            product_name=product_name,
            quantity=quantity,
            price=price,
            product_image=filename
        )
        db.session.add(new_product)
        db.session.commit()
        
        return redirect(url_for("products.new_products"))

    return render_template("new_products.html", categories=categories, socks_categories=socks_categories)


@products.route('/products/img/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(os.path.abspath(os.getcwd()), 'app', 'products', 'img'), filename)