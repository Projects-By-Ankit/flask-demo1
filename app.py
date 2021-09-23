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
def default():
    msghelp = {"Available End Points are: ": ["/ping",
                                              "",
                                              """/register-user?name=<Enter Your Name>&ph_no=<Enter Your Phone 
                                              Number> &mail_id=<Enter Your Mail_Id>&user_id=<Enter the user id 
                                              you want> &password=<Your Password>&c_password=<Confirm Password>""",
                                              "",
                                              "/login?user_id=<Your User Id>&password=<Your Password>",
                                              "",
                                              "/getdata?uname=<Your User Name>",
                                              "",
                                              """/updatedata?site_u_name=<Your Website User Name>&u_pass=<Your 
                                              Site Password>&u_name=<Your MRG User Name>&site_name=<Which 
                                              Web-Site You Want To Update>&id_num=<Website Id Number> """,
                                              "",
                                              """/deletedata?u_name=<Your MRG User Name>&site_name=<Which 
                                              Web-Site You Want To Delete>&id_num=<Website Id Number> """
                                              ]}

    return jsonify(msghelp)


# def hello_world():
#     try:
#         dict1 = {}
#         mycursor = conn.cursor()
#         mycursor.execute("SELECT * FROM data_table WHERE user_name=%s", (request.args.get("name"),))
#         data = mycursor.fetchall()
#         for row in range(len(data)):
#             temp = data[row]
#             dict1[row] = {"user_name": temp[0],
#                           "site_name": temp[1],
#                           "site_id_name": temp[2],
#                           "site_password": temp[3],
#                           "id_number": temp[4],
#                           }
#         return make_response(jsonify(dict1))
#
#     except Exception as e:
#         print(e)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
