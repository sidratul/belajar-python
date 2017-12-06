from mysql.connector.pooling import MySQLConnectionPool

class MysqlConn:

	dbconfig = {
	  	"database": "pythontest",
	  	"user":     "root",
	  	"password" : "admin"
	}
	
	conn = MySQLConnectionPool(
		pool_name = "mypool",
        pool_size = 5,
        **dbconfig
    )

	def getConn(self):
		return self.conn.get_connection()
