from flask_restful import Resource
class SomeClass(Resource):

	def get(self):
		return { 'data' : ['data','from','imported','class'] }