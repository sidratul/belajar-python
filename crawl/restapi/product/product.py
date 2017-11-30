from flask_restful import Resource
from database import Database

class Product(Resource):

	database = Database()
	selectSql = "SELECT * FROM `product` WHERE 1"
	insertSql = "INSERT INTO `product` (`product_name`, `product_price`) VALUES (%(product_name)s,%(product_price)s)"

	def get(self):
		conn = self.database.getConn()
		cursor = conn.cursor()
		cursor.execute(self.selectSql)
		
		products = []

		for product in cursor:
		  	products.append({
		  		"id" : product[0],
		  		"product_name" : product[1],
		  		"product_price" : product[2],
		  	})

		cursor.close()
		conn.close()
		return {
			"products" : products
		}

	def post(self):
		conn = self.database.getConn()
		cursor = conn.cursor()
		dataProduct = {
		  'product_name': 'product mantap',
		  'product_price': 55000,
		}
		cursor.execute(self.insertSql,dataProduct)
		conn.commit()
		cursor.close()
		conn.close()
		return cursor 
