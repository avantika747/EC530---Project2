from flask import Flask, request, jsonify

app = Flask(__name__)

# sample authentication to implement any authentication logic
def authenticate(token):
  if token == 'actual_token':
    return True
  else:
    return False

# device data
devices = []

# API endpoints - CRUD operations
@app.route('/devices', methods=['GET'])
def get_devices():
  # authenticate the user
  token = request.headers.get('Authorization')
  if not authenticate(token):
    return jsonify({'error': 'Unauthorized access'}), 401
  # retrieving and returning the list of devices
  return jsonify(devices), 200

@app.route('/devices', methods=['POST'])
def register_device():
  # authenticate the user
  token = request.headers.get('Authorization')
  if not authenticate(token):
    return jsonify({'error': 'Unauthorized access'}), 401
    
  # parse request and register device
  data = request.json
  if 'name' not in data or 'type' not in data:
        return jsonify({'error': 'Missing name or type in request'}), 400

  # add device to devices list
  devices.append(data)
  return jsonify({'message': 'Device registered successfully'}), 201

@app.route('/devices/<device_id>', methods=['PUT'])
def update_device(device_id):
  # authenticate the user
  token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({'error': 'Unauthorized access'}), 401
  
  # find device ID and update information
  for device in devices:
        if device.get('id') == device_id:
            # update device information
            data = request.json
            device.update(data)
            return jsonify({'message': 'Device updated successfully'}), 200
        return jsonify({'error': 'Device not found'}), 404

@app.route('/devices/<device_id>', methods=['DELETE'])
def delete_device(device_id):
  # authenticate the user
  token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({'error': 'Unauthorized access'}), 401
  
  # find device ID and delete information
  for device in devices:
        if device.get('id') == device_id:
            devices.remove(device)
            return jsonify({'message': 'Device deleted successfully'}), 200
        return jsonify({'error': 'Device not found'}), 404
        
if __name__ == '__main__':
    app.run(debug=True)




