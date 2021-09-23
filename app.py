from flask import Flask, jsonify, request, make_response

app = Flask(__name__)


@app.route("/")
def hello_world():
    msg = {"Status": "Alive"}
    return make_response(jsonify(msg, 200))


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
