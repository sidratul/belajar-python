from mysql.connector.pooling import MySQLConnectionPool

class Database:

	dbconfig = {
	  	"database": "pythontest",
	  	"user":     "root",
	  	"password" : "admin"
	}
	
	conn = MySQLConnectionPool(
		pool_name = "mypool",
        pool_size = 2,
        **dbconfig
    )

	def getConn(self):
		return self.conn.get_connection()