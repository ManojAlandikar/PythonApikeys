
import mysql.connector
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import json
from flask_bcrypt import Bcrypt
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


   def user_ADDNEW_model(self,data):
    try:
        data = request.get_json()

        # Hash the password before storing it
        hashed_password = Bcrypt().generate_password_hash(data['password']).decode('utf-8')

        query = """
            INSERT INTO new_table (name, role, designation, username, password)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (data['name'], data['role'], data['designation'], data['username'], hashed_password)

        self.cur.execute(query, values)
        self.con.commit()

        # Get the last inserted ID
        self.cur.execute("SELECT LAST_INSERT_ID() as id")
        result = self.cur.fetchone()
        inserted_id = result['id']

        # Get the current user identity
        current_user = get_jwt_identity()

        return {'id': inserted_id, 'name': data['name'], 'role': data['role'], 'username': data['username']}
    except Exception as e:
        # Handle exceptions (log the error, return an error response, etc.)
        print(f"Error: {str(e)}")
        return {'error': 'An error occurred while adding a new member'}, 500
    finally:
        # Close the cursor (and optionally the connection)
        self.cur.close()
        # self.conn.close()  # Uncomment this line if you want to close the connection as well
  
   def user_update_model(self,data): #to update member in table
       self.cur.execute(f"UPDATE new_table SET name='{data['name']}',role ='{data['role']}',designation='{data['designation']}' WHERE id={data['id']} ")
       current_user = get_jwt_identity()
       if self.cur.rowcount>0:
         return "data updated Successfully"
       else:
           return " data updated Unsuccessfully"
       
'''
   def user_delete_model(self,id):  #to delete an employee detail
       self.cur.execute(f"DELETE from new_table WHERE id={id}")
       current_user = get_jwt_identity()
       if self.cur.rowcount>0:
         return "data deleted  Successfully"
       else:
           return " data deleted Unsuccessfully"
       

   def user_patch_model(self,data ,id):  #to do the patch work in database
       self.cur.execute(f"DELETE from new_table WHERE id={id}")
       current_user = get_jwt_identity()
       if self.cur.rowcount>0:
         return "data deleted  Successfully"
       else:
           return " data deleted Unsuccessfully"
    
   def authenticate():
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        if username in new_table and username[username]['password'] == password:
        # Authentication successful
            return jsonify({"success": True, "message": "Authentication successful"})
        else:
        # Authentication failed
            return jsonify({"success": False, "message": "Authentication failed"})


          
     
   def user_getall_model(self):  #to read the data in mysql sheet
       self.cur.execute("SELECT * FROM new_table")
       result= self.cur.fetchall()
       current_user = get_jwt_identity()
       return json.dumps(result) 
       '''
