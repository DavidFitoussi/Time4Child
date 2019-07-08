from flask import Flask
from flask_restful import Api, Resource , reqparse
from flask_cors import CORS
from Resource import clsResource

app  = Flask(__name__)
CORS(app)
api = Api(app)

class Service (Resource):
    @app.route('/index')
    def index():
        return "Hello, david!"

    @app.route('/GetTimeofuser')
    def GetTimeofuser():
        InstanceResource = clsResource()
        result = str(InstanceResource.GetLastTime())
        return result,200


    @app.route('/GetUserName')
    def GetUserName():
        InstanceResource = clsResource()
        result = str(InstanceResource.username)
        return result,200



api.add_resource(Service)

app.run(debug=True)









