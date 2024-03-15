# implementing a sample REST API for the authentication/authorization module
# of the remote health monitoring system

from flask import Flask, request, jsonify

# sample data stored as dict here (can be modelled into a database) 
users = {"user1" : {
         "password" : "abcde",
         "permissions" : ["read", "write", "edit"]
        }
}

# authentication API endpoint - POST method
@app.route('/auth/login', methods=['POST'])

# login function
def login():
  data = request.json
  username = data.get('username')
  password = data.get('password')

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
         
