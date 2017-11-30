from flask_restful import Resource
from database import Database

class Product(Resource):

	database = Database()
	selectSql = "SELECT * FROM `product` WHERE 1"
	insertSql = "INSERT INTO `product` (`product_name`, `product_price`) VALUES (%(product_name)s,%(product_price)s)"

	def get(self):
		conn = self.database.getConn()
		cursor = conn.cursor()


	def post(self):
		conn = self.database.getConn()
		cursor = conn.cursor()
		dataProduct = {
		  'product_name': 'product keren',
		  'product_price': 55000,
		}
		res = cursor.execute(self.insertSql,dataProduct)
		conn.commit()
		cursor.close()
		conn.close()
		return res 
