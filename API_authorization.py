# implementing a sample REST API for the authentication/authorization module
# of the remote health monitoring system

from flask import Flask, request, jsonify
import re

# sample data stored as dict here (can be modelled into a database) 
users = {"user1" : {
         "password" : "abcde",
         "permissions" : ["read", "write", "edit"]
        }
}

# authentication API endpoint - POST method
@app.route('/auth/login', methods=['POST'])

# input sanitization 
# making sure that the username and password entered is only alphanumeric with underscores
def validate_username(username):
         return re.match(r"^[a-zA-Z0-9_]{3,20}$", username) is not None

# making sure that the length of the password is greater than 6 characters
def validate_password(password):
         return len(password) >= 6

# login function
def login():
  data = request.json
  username = data.get('username')
  password = data.get('password')

  if not validate_username(username):
           return jsonify({'error': 'Invalid username'}), 400

  if not validate_password(password):
           return jsonify({'error': 'Invalid password'}), 400
         
  if username in users and users[username]['password'] == password:
        # authentication successful, generate and return access token
        access_token = generate_access_token(username)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

# authorization API endpoint - GET method
@app.route('/auth/authorize', methods=['GET'])
def authorize():
    token = request.args.get('token')
    permission = request.args.get('permission')

    username = validate_access_token(token)
    if username:
        user_permissions = users.get(username, {}).get('permissions', [])
        if permission in user_permissions:
            return jsonify({'message': 'Authorization successful'}), 200
        else:
            return jsonify({'error': 'Forbidden'}), 403
    else:
        return jsonify({'error': 'Unauthorized'}), 401

def generate_access_token(username):
    return "<randomly_generated_access_token>"

def validate_access_token(token):
    # returns username if token is valid, otherwise None
    return "<username>" if token == "<randomly_generated_access_token>" else None

if __name__ == '__main__':
    app.run(debug=True)
         
