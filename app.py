from flask import Flask, jsonify, request, make_response
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(
    host="sql5.freesqldatabase.com",
    user="sql5438699",
    password="Ektwg1xgFv",
    database="sql5438699"
)
mycursor = conn.cursor()


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


@app.route("/register-user")
def register_user():
    global flag1
    global flag2
    try:
        mycursor.execute("SELECT * FROM login_data")
        data = mycursor.fetchall()
        for row in range(len(data)):
            temp = data.__getitem__(row)
            if temp[3] == request.args.get("user_id").strip():
                flag1 = False
                break
            else:
                flag1 = True
        if request.args.get("password").strip() == request.args.get("c_password").strip():
            flag2 = True
        else:
            flag2 = False

        if flag1 and flag2:
            mycursor.execute(
                "INSERT INTO login_data (name,ph_no,mail_id,user_name,password,c_password) VALUES (%s, %s, %s, %s, %s, %s)",
                (request.args.get("name"), request.args.get("ph_no"), request.args.get("mail_id"),
                 request.args.get("user_id"),
                 request.args.get("password"), request.args.get("c_password"),))
            conn.commit()

            return jsonify([True, "...User Created Successfully..."])
        elif flag2 and not flag1:
            return jsonify([False, "...User Name Taken..."])
        elif flag1 and not flag2:
            return jsonify([False, "...Password And Confirm Password Not Same..."])
    except Exception as e:
        print(e)


@app.route("/login")
def logindata():
    try:
        flag = False
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM login_data")
        data = mycursor.fetchall()

        for row in range(len(data)):
            temp = data.__getitem__(row)
            if temp[3] == request.args.get("user_id").strip() and temp[4] == request.args.get("password").strip():
                return jsonify([True, temp[3], "...Login Successful..."])
                flag = True
                break
            else:
                flag = False

        if not flag:
            return jsonify([False, "...Login Failed..."])
    except Exception as e:
        print(e)



if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
