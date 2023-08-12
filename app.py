from flask import Flask, request
from mysql import connector
import json

from constants import host, database, user, password
from Login_Signup import login, signup


app = Flask(__name__)

@app.route('/')
def home_page():
    return 'hello there'


@app.route("/login/", methods=['GET'])
def login_page():
    id = request.args.get("id") #/user/?user=user name
    paswrd = request.args.get("password")

    status, msg, name, token = login.check_user_exist(id, paswrd)

    json_data = {'status': status, "message": msg, 'name': name, 'token': token}
    return json_data

@app.route("/signup/", methods=['GET'])
def signup_page():
    id = request.args.get('id')
    paswrd = request.args.get('password')
    name = request.args.get("name")
    email = request.args.get("email")
    dob = request.args.get('dob')

    status, ans = signup.signup(id, paswrd, name, email, dob)
    json_data = {'status': status, "msg": ans}
    return json_data


if __name__=='__main__':
    app.run(debug=True)