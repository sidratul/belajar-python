from db.mysql_conn import MysqlConn

class UrlMysqlDao:

	database = MysqlConn()
	insertSql = "REPLACE INTO `urls` ( `url`, `keywords` ) VALUES (%s,%s)"

	def insert(self,params):
		conn = self.database.getConn()
		cursor = conn.cursor()
		cursor.execute(self.insertSql,params)
		conn.commit()
		cursor.close()
		conn.close()

	def insert_many_url_same_keyword(self,keyword,urls):
		conn = self.database.getConn()
		cursor = conn.cursor()

		for url in urls:
			cursor.execute(self.insertSql,(url,keyword))

		conn.commit()
		cursor.close()
		conn.close()
