from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Help(Resource):
    def get(self):
        msg = {"Status": "Alive"}
        return make_response(jsonify(msg, 200))


#
# @app.route("/")
# def hello_world():
#     return "Hello and Welcome to Flask App"

api.add_resource(Help, "/")

# if __name__ == "__main__":
app.run(debug=False, host="0.0.0.0")
