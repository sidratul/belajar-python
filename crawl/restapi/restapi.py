from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from mysql.connector import (connection)

from SomeClass import SomeClass
from product.product import Product
from database import Database

app = Flask(__name__)
api = Api(app)

class Employees(Resource):
	def get(self):
		return { "employees" : ["some","data"] }


api.add_resource(Employees, '/employees')
api.add_resource(SomeClass, '/other')
api.add_resource(Product, '/product')

@app.route('/test')
def bedaNama():
    return 'Ini Test Page'


if __name__ == '__main__':
	app.run(port='5002')