from app import create_app, db
from app.models import Category, SocksCategory
app = create_app()

def category():
    category_names = ["Dama", "Caballero", "Kids"]
    for name in category_names:
        # Check if the category already exists
        existing_category = Category.query.filter_by(category_name=name).first()
        if not existing_category:
            cate = Category(category_name=name)
            db.session.add(cate)
    db.session.commit()


def socks_category_func():
    socks_categories = [ "Media Larga", "Media 3/4", "Media Tobillera", "Media Disney", "Media Deportiva", "Media Talonera", "Media Colegial", "Media Subliminada", "Media Tobillera Nike", "Media Tobillera Adidas"]
    for x in socks_categories:
        e = SocksCategory.query.filter_by(socks_category_name=x).first()
        if not e:
            new_socks_category = SocksCategory(socks_category_name=x)
            db.session.add(new_socks_category)
    db.session.commit()



if __name__ == "__main__":
    # app.app_context().push()
    # db.create_all()
    # category()
    # socks_category_func()
    app.run(debug = True, port = 7000, host='0.0.0.0')