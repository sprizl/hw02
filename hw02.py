from flask import Flask , request
from flask_restful import Resource , Api,reqparse
import json , time

app = Flask (_name_)
api = Api(app)
APP_ROOT =os.path.dirname()

parser = reqparse.RequestParser()
parser.add_argument('info')
class Hello(Resource):
	def post(self):
		args = parser.parse_args()
		name = args['info']
		x = name.split('-')
		age = 0
		if(time.gmtime()[1] - int(x[1])>=0):
			if(time.gmtime()[0] - int(x[0]) >= 0):
				age = age + 1
		age = age + (time.gmtime().tm_year - int(x[2]))
		if(age >= 0):
			return{"birthday":name ,"Age":age}
		else:
			return{"you are not born yet."}

api.add_resource(Hello,'/timestamp')

if _name_ == '_main_':
	app.run(host='0.0.0.0',port = 5500)
