from flask import Flask
# from flask_restful import Api
from application.config import Config
from application.data.database import db
from flask_security import Security, SQLAlchemySessionUserDatastore
from application.data.models import User, Role

api = None
app = None

def create_app():
    app = Flask(__name__, template_folder = 'templates')
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)
    app.app_context().push()
    return app, api

app, api = create_app()

from application.controller.controller import *

from application.controller.api import *

api.add_resource(UserAPI, "/role")
api.add_resource(AllCategoryAPI, "/allcategory")
api.add_resource(CategoryAPI, "/category/<int:categoryid>", "/category")
api.add_resource(AllProductAPI, "/products/<int:categoryid>")
api.add_resource(CategoryNameAPI, "/categoryname/<int:categoryid>")
api.add_resource(ProductAPI, "/product/<int:productid>", "/product")
api.add_resource(CartAPI, "/cart/<int:productid>", "/cart")
api.add_resource(PurchaseAPI, "/purchase/<int:cartid>", "/purchase")
api.add_resource(CartCountAPI, "/cartcount")
api.add_resource(PurchaseAllAPI, "/purchaseall")
api.add_resource(SearchPAPI, "/search/<string:search>/<int:sort>")
api.add_resource(SearchCAPI, "/searchc/<string:search>")
api.add_resource(RequestCategoryAPI, "/requestc/<string:categoryname>", "/requestc")
api.add_resource(ManagerRegisterAPI, "/requestm")
api.add_resource(UserRegisterAPI, "/register/<string:username>")
api.add_resource(DashboardAPI, "/dashboard")

if __name__ == '__main__':
    app.run()
