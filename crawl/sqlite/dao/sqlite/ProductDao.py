from dao.sqlite.SqliteConn import SqliteConn
from pprint import pprint

class ProductDao:

	sqlConn =  SqliteConn()
	testInsertSql = "INSERT INTO product (name,description,price) VALUES ('product bagus','product yang bagus',24000)" 
	insertSql = "INSERT INTO product (name,description,price) VALUES (:name,:description,:price)" 
	selectSql = "SELECT * FROM product"
	updateSql = "UPDATE product SET name=:name,description=:description,price=:price WHERE id=:id"

	def __init__(self):
		return

	def getProducts(self):
		c = self.sqlConn.getCursor()
		c.execute(self.selectSql)
		return c.fetchall()

	def insertProduct(self,params):
		self.sqlConn.execute(self.insertSql,params)
		return "success insert"

	def updateProduct(self,params):
		c = self.sqlConn.getCursor()
		c.execute(self.updateSql,params)

		if(c.rowcount != 1)
			self.sqlConn.close()
			return "update failed"
		
		self.sqlConn.commit()
		self.sqlConn.close()
		return "update success"

	def testInsert(self):
		c = self.sqlConn.getCursor()
		c.execute(self.testInsertSql)

		self.sqlConn.commit()
		self.sqlConn.close()

		return "berhasil insert"
	