import sqlite3
import os

class SqliteConn:
	

	def __init__(self):
		self.conn = sqlite3.connect(os.getcwd()+'/demoztool.db',check_same_thread = False)
		return

	def get_conn(self):
		return self.conn

	def get_cursor(self):
		return self.get_conn().cursor()

	def close(self):
		self.conn.close()

	def commit(self):
		self.conn.commit()

	def fecth_all(self,query,params=()):
		c = self.get_cursor()
		c.execute(query,params)
		res = c.fetchall()
		self.commit()

		return res

	def fecth_one(self,query,params=()):
		c = self.get_cursor()
		c.execute(query,params)
		res = c.fetchone()
		self.commit()

		return res

	def execute(self,query,params=()):
		c = self.get_cursor()
		c.execute(query,params)
		count = c.rowcount
		self.commit()
		
		return count

	def execute_many(self,query,params):
		c = self.get_cursor()
		self.execute_many(query,params)
		count = c.rowcount
		self.commit()

		return count

	def __del__(self):
		self.conn.close()
