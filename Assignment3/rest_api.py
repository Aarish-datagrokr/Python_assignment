from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from Models import db
from Views import CustomersView, CustomerView, OrdersView, ProductsView, OrderView, ProductView, OrderHistoryView

database_app = Flask(__name__)

database_app.config.from_object('config')

db.init_app(database_app)

api = Api(database_app)

database_app.app_context().push()


@database_app.before_first_request
def create_table():
    db.create_all()


api.add_resource(CustomersView, '/customers')
api.add_resource(CustomerView, '/customer/<string:CustomerID>')

api.add_resource(OrderHistoryView, '/orderhistory/<string:CustomerID>')

api.add_resource(OrdersView, '/orders')
api.add_resource(OrderView, '/order/<int:OrderID>')

api.add_resource(ProductsView, '/products')
api.add_resource(ProductView, '/product/<string:ProductID>')

if __name__ == "__main__":
    database_app.run(debug=True)