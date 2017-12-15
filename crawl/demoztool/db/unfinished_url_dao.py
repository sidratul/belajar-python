from db.sqlite_conn import SqliteConn

class UnfinishedUrlDao:
	conn =  SqliteConn()

	create_sql = "CREATE TABLE IF NOT EXISTS unfinished_urls (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT UNIQUE, node_count INTEGER, input_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP )"
	select_sql = "SELECT * FROM unfinished_urls WHERE 1"
	insert_sql = "REPLACE INTO unfinished_urls (url,node_count) VALUES (?,?)"
	delete_sql = "DELETE FROM unfinished_urls WHERE url = ?"
	truncate_sql = "DELETE FROM unfinished_urls"

	def __init__(self):
		self.conn.execute(self.create_sql)

	def get_all(self):
		return self.conn.fecth_all(self.select_sql)

	def insert(self,url,node_count):
		return self.conn.execute(self.insert_sql,(url,node_count))

	def delete_by_url(self,url):
		return self.conn.execute(self.delete_sql,[url])

	def trucate(self):
		return self.conn.execute(self.truncate_sql)