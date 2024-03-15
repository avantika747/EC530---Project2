# Implementation of a sample REST API for user management
# demonstrating basic crud operations

from flask import Flask, request, jsonify

# creating sample data as a dictionary - this can be modelled into a database 
users = {
  "user1" : {
    "username" : "harrypotter",
    "password" : "deathlyhallows",
    "email" : "harrypotter@hogwarts.edu",
    "role" : "patient"
  }
  "user2" : {
    "username" : "jakeperalta",
    "password" : "b99",
    "email" : "jp@b99.com",
    "role" : "doctor"
  }
}

# API endpoint to get all users
@app.route('/users', methods = ['GET'])
def get_users():
    return jsonify(users), 200

# API endpoint to get a specific user
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    if username in users:
        return jsonify(users[username]), 200
    else:
        return jsonify({'error': 'User not found'}), 404

# API endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    if username in users:
        return jsonify({'error': 'Username already exists'}), 400

    # creating new user
    users[username] = {
        "username": username,
        "password": data.get('password'),
        "email": data.get('email'),
        "role": data.get('role', 'user')
    }
    return jsonify(users[username]), 201

# API endpoint to update an existing user
@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    if username not in users:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    users[username]['password'] = data.get('password', users[username]['password'])
    users[username]['email'] = data.get('email', users[username]['email'])
    users[username]['role'] = data.get('role', users[username]['role'])

    return jsonify(users[username]), 200

# API endpoint to delete an existing user
@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    if username not in users:
        return jsonify({'error': 'User not found'}), 404

    del users[username]
    return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
  
