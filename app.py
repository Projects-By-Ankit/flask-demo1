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
    msghelp = {"Available End Points are: ": [{"ping": "/ping",
                                               "Register New User": """/register-user?name=<Enter Your Name>&ph_no=<Enter Your Phone Number> &mail_id=<Enter Your Mail_Id>&user_id=<Enter the user id you want> &password=<Your Password>&c_password=<Confirm Password>""",
                                               "Login": "/login?user_id=<Your User Id>&password=<Your Password>",
                                               "Insert Data": """/insert_data?user_name=<Enter Your MSR User Name>&site_name=<Enter site name>&site_user_name=<Enter Site User Name>&site_password=<Enter Website Password>&id_number=<Account ID Number>""",
                                               "Get Data": "/getdata?uname=<Your User Name>",
                                               "Update Data": """/updatedata?site_u_name=<Your Website User Name>&u_pass=<Your Site Password>&u_name=<Your MRG User Name>&site_name=<Which Web-Site You Want To Update>&id_num=<Website Id Number> """,
                                               "Delete Data": """/deletedata?u_name=<Your MRG User Name>&site_name=<Which Web-Site You Want To Delete>&id_num=<Website Id Number> """}]}

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
                (request.args.get("name").strip(), request.args.get("ph_no").strip(),
                 request.args.get("mail_id").strip(),
                 request.args.get("user_id").strip(),
                 request.args.get("password").strip(), request.args.get("c_password").strip(),))
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


@app.route("/insert_data")
def insertdata():
    try:
        mycursor.execute("SELECT * FROM data_table")
        data = mycursor.fetchall()
        for row in range(len(data)):
            temp = data.__getitem__(row)
            if temp[0] == request.args.get("user_name").strip() and temp[1] == request.args.get("site_name").strip() and \
                    temp[
                        4] == request.args.get("id_number").strip():
                flag1 = False
                break
            else:
                flag1 = True
        if flag1:
            mycursor.execute(
                "INSERT INTO data_table (user_name,site_name,site_user_name,site_password,id_number) VALUES(%s,%s,%s,%s,%s)",
                (request.args.get("user_name").strip(), request.args.get("site_name").strip(),
                 request.args.get("site_user_name").strip(),
                 request.args.get("site_password").strip(), request.args.get("id_number").strip()))
            conn.commit()
            return jsonify([True, "...Data Inserted Successfully..."])
        else:
            return jsonify([False, "...Data Duplication Error..."])
    except Exception as e:
        print(e)


@app.route("/getdata")
def getdata():
    try:
        dict1 = {}
        mycursor.execute("SELECT * FROM data_table WHERE user_name=%s", (request.args.get("uname").strip(),))
        data = mycursor.fetchall()
        for row in range(len(data)):
            temp = data.__getitem__(row)
            dict1[row] = {"user_name": temp[0],
                          "site_name": temp[1],
                          "site_id_name": temp[2],
                          "site_password": temp[3],
                          "id_number": temp[4],
                          }
        return jsonify(dict1)
    except Exception as e:
        print(e)


@app.route("/updatedata")
def updatedata():
    try:
        mycursor.execute(
            """UPDATE data_table SET site_user_name=%s,site_password=%s WHERE user_name=%s AND site_name=%s AND 
                            id_number=%s""",
            (request.args.get("site_u_name").strip(), request.args.get("u_pass").strip(),
             request.args.get("u_name").strip(),
             request.args.get("site_name").strip(), request.args.get("id_num").strip()))
        conn.commit()
        if mycursor.rowcount > 0:
            return jsonify([True, "...Data Updated Successfully..."])
        else:
            return jsonify([False, "...No Rows Affected..."])
    except Exception as e:
        print(e)


@app.route("/deletedata")
def deletedata():
    try:
        mycursor = conn.cursor()
        print(
            mycursor.execute(
                """DELETE FROM data_table WHERE user_name=%s AND site_name=%s AND 
                id_number=%s""",
                (request.args.get("u_name").strip(), request.args.get("site_name").strip(), request.args.get("id_num").strip(),)))
        conn.commit()
        if mycursor.rowcount > 0:
            return jsonify([True, "...Data Deleted Successfully..."])
        else:
            return jsonify([False, "...No Rows Affected..."])


    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
