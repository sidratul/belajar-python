from flask import Flask, request
from dao.sqlite.ProductDao import ProductDao
import os
from json import dumps,loads
from pprint import pprint

app = Flask(__name__)
productDao = ProductDao()

@app.route('/products')
def getProducts():
    return dumps(productDao.getProducts())

# {
# 	"name" : "product keren",
# 	"description" : "product yang keren",
# 	"price" : "30000"
# }
@app.route('/insertProduct',methods=['POST'])
def insertProducts():
    return productDao.insertProduct( loads(request.data) )

@app.route('/updateProduct',methods=['POST'])
def updateProduct():
    return productDao.updateProduct( loads(request.data) )

@app.route('/testInsert')
def testInsert():
	# pprint(vars(request))
    return productDao.testInsert();


if __name__ == '__main__':
	app.run(port='5002')