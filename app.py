from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(
    host="sql5.freesqldatabase.com",
    user="sql5438699",
    password="Ektwg1xgFv",
    database="sql5438699"
)


@app.route("/")
def hello_world():
    try:
        dict1 = {}
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM data_table WHERE user_name=%s", (request.args.get("name"),))
        data = mycursor.fetchall()

        for row in range(len(data)):
            temp = data.__getitem__(row)
            dict1[row] = {"user_name": temp[0],
                          "site_name": temp[1],
                          "site_id_name": temp[2],
                          "site_password": temp[3],
                          "id_number": temp[4],
                          }
            return make_response(jsonify(dict1))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
