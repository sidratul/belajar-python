from db.sqlite_conn import SqliteConn

class UrlDao:
	conn =  SqliteConn()

	create_sql = "CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT UNIQUE,last_update VARCHAR(100), node_count INTEGER )"
	select_sql = "SELECT * FROM urls WHERE 1"
	exist_sql = "SELECT * FROM urls WHERE url=? AND node_count = ?"
	insert_sql = "REPLACE INTO urls (url,node_count,last_update) VALUES (?,?,?)"
	delete_sql = "DELETE FROM urls WHERE id = ?"
	truncate_sql = "DELETE FROM urls"

	def __init__(self):
		return conn.execute(self.create_sql)

	def get_all(self):
		return conn.fecth_all(self.select_sql)

	def is_url_exist(self,url,node_count):
		return self.conn.fecth_one(self.exist_sql,(url,node_count))
		
	def insert(self,url,node_count,last_update):
		return self.conn.execute(self.insert_sql,(url,node_count,last_update))

	def delete(self,id):
		return self.conn.execute(self.delete_sql,(id))

	def trucate(self):
		return self.conn.execute(self.truncate_sql)

	def createTable(self):
		return self.conn.execute(self.create_sql)