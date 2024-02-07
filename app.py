
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
import mysql.connector
import bcrypt

app = Flask(__name__)

# Replace 'your_username', 'your_password', and 'your_database' with your MySQL credentials
db = mysql.connector.connect(host="localhost", user="root", password="", database="company_db")

app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

def verify_password(passwordd, password):
    return bcrypt.checkpw(passwordd.encode('utf-8'), password.encode('utf-8'))

def get_hashed_password_from_db(username):
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT password FROM new_table WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return result['password']
        else:
            return None
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return None

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        passwordd = data.get('password')

        password_from_db = get_hashed_password_from_db(username)

        if password_from_db and verify_password(passwordd, password_from_db):
            # Password is correct, create and return the access token
            access_token = create_access_token(identity=username)
            return {'access_token': access_token}
        else:
            # Password is incorrect or user not found
            return jsonify({"msg": "The password is incorrect!"}), 401

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"msg": "Internal Server Error"}), 500
from projest.user_controller import user_model
if __name__ == '__main__':
    app.run(debug=True)
