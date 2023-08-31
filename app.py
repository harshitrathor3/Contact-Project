from flask import Flask, request, jsonify
from mysql import connector
import json

from constants import host, database, user, password
from Login_Signup import login, signup
from Application import contacts_display, groups_display, upload_contacts


app = Flask(__name__)

@app.route('/')
def home_page():
    return '<h2>hello there</h2>'


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

@app.route('/applications/get_contacts/', methods=['GET'])
def get_contacts():
    id = request.args.get('id')
    token = request.args.get('token')
    print(id, token)
    status, msg, data = contacts_display.display_contacts(id, token)
    json_data = {'status': status, "msg": msg, 'data': data}
    return json_data

@app.route('/applications/get_groups/', methods=['GET'])
def get_groups():
    id = request.args.get('id')
    token = request.args.get('token')
    status, msg, data = groups_display.display_groups(id, token)

    json_data = {'status': status, "msg": msg, 'data': data}
    return json_data

@app.route('/applications/upload_contact/', methods=['POST'])
def upload_contact():
    json_data = request.json
    

    status, msg = upload_contacts.upload(json_data)
    return jsonify({'status': status, 'msg': msg})
    
    












if __name__=='__main__':
    app.run(debug=True)