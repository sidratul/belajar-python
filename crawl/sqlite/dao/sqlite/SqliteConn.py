import sqlite3
import os


class SqliteConn:
	
	def __init__(self):
		return

	def getConn(self):
		self.conn = sqlite3.connect(os.getcwd()+'/test.db')
		return self.conn

	def getCursor(self):
		return self.getConn().cursor()

	def close(self):
		self.conn.close()

	def commit(self):
		self.conn.commit()

	def execute(self,query,params):
		c = self.getCursor()
		c.execute(query,params)
		self.commit()
		self.close()

	def executeMany(self,query,params):
		c = self.getCursor()
		self.executemany(query,params)
		self.commit()
		self.close()

	@staticmethod 
	def getConnection(self):
		return self.conn