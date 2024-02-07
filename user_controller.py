
import mysql.connector
import json
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_mysqldb import MySQL
from flask import Flask, jsonify ,request , make_response
from app import app
from projest.user_model import user_model
from flask import request


app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)
obj =  user_model()
'''
class user_model():
   def __init__(self):
      try:
          self.con=mysql.connector.connect(host="localhost",user="root",password="",database="company_db")
          #in futer if u add any queare then that will be added atomatically 
          self.con.autocommit=True
          self.cur=self.con.cursor(dictionary=True)
          print("running successfully")
      except:
          print("not running currectly")
'''
@app.route("/user/getall")
@jwt_required()

def user_getall_model(self):  #to read the data in mysql sheet
                 self.cur.execute("SELECT * FROM new_table")
                 result= self.cur.fetchall()
                 current_user = self.get_jwt_identity()
       #return {'message': f'Hello, {current_user}! You have access to this protected resource.'}
                 return obj.user_getall_model(request.form)

         #return json.dumps(result) 
    

@app.route("/user/addnew",methods=["POST"])
@jwt_required()
         
def user_ADDNEW_model(): #to add new member in table
           
            return obj.user_ADDNEW_model(request.form) 

@app.route("/user/update",methods=["PUT"])
@jwt_required()
def user_update_controller():
           return obj.user_update_model(request.form)

@app.route("/user/delete/<id>",methods=["DELETE"])
@jwt_required()
def user_delete_controller(id):
    return obj.user_delete_model(id)

@app.route("/user/patch/<id>",methods=["PATCH"])
@jwt_required()
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id)

    '''
import mysql.connector
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_mysqldb import MySQL
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'company_db'
mysql = MySQL(app)

# Initialize JWTManager after creating the Flask app instance
jwt = JWTManager(app)

class UserModel:
    def __init__(self):
        try:
            self.con = mysql.connection
            self.cur = self.con.cursor(dictionary=True)
            print("Running successfully")
        except Exception as e:
           print(f"Error connecting to MySQL: {e}")


    def user_getall_model(self):
        try:
            self.cur.execute("SELECT * FROM new_table")
            result = self.cur.fetchall()
            current_user = get_jwt_identity()
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)})

    def user_ADDNEW_model(self):
        try:
            data = request.form
            self.cur.execute(f"INSERT INTO new_table(id, name, role, designation, username, password) VALUES('{data['id']}','{data['name']}', '{data['role']}','{data['designation']}','{data['username']}','{data['password']}')")
            print(data)
            current_user = get_jwt_identity()
            return jsonify({'message': 'User added successfully'})
        except Exception as e:
            return jsonify({'error': str(e)})

# Routes outside the class
obj = UserModel()

@app.route("/user/getall")
@jwt_required()
def get_all_users():
    return obj.user_getall_model()

@app.route("/user/addnew", methods=["POST"])
@jwt_required()
def add_new_user():
    return obj.user_ADDNEW_model()

# Run the Flask app if this file is executed
if __name__ == "__main__":
    app.run(debug=True)

'''
