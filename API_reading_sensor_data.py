from flask import Flask, request, jsonify

app = Flask(__name__)

# sample authentication
def authenticate(token):
  if token == 'provided_token': # sample token
        return True
    else:
        return False

@app.route('/sensor-data', methods=['POST']) # using POST method
def sensor_data():
    # taking the access token from the request headers
    token = request.headers.get('Authorization')

    # authenticating the user
    if not authenticate(token):
        return jsonify({'error': 'Authentication failed'}), 401

    # parsing the request body
    data = request.json

    # validating the request body
    if not data or 'sensor_id' not in data or 'timestamp' not in data or 'data' not in data:
        return jsonify({'error': 'Invalid request body'}), 400

    # processing the sensor data
    sensor_id = data['sensor_id']
    timestamp = data['timestamp']
    sensor_data = data['data']

    # final success message
    return jsonify({'message': 'Data Received!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
