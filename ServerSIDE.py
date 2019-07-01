from flask import Flask
from flask_restful import Api, Resource , reqparse

app  = Flask(__name__)
api = Api(app)


class Service (Resource):
    @app.route('/index')
    def index():
        return "Hello, david!"

    @app.route('/GetTimeofuser')
    def GetTimeofuser():
      return main.GetLastTime(),200


api.add_resource(Service, "/user/<string:name>")
app.run(debug=True)









