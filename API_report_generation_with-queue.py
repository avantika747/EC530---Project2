# implementing a sample REST API for report generation with queues to process the same

from flask import Flask, request, jsonify
from queue import Queue
from threading import Thread

app = Flask(__name__)

# sample user data as dictionary (to be replaced with database)
users = {
    "atticusfinch" : {
        "password" : "justice"
    }
}

# medical report generation queue
report_queue = Queue() # initializing queue

# worker function to process report generation tasks (this report_worker segment's idea borrowed from ChatGPT)
def report_worker():
    while True:
        task = report_queue.get()
        if task is None:
            break

        # process report generation task
        generate_report(task['patient_id'], task['report_data'])
        report_queue.task_done()

# starting the thread
report_thread = Thread(target=report_worker)
report_thread.daemon = True
report_thread.start()

# API authentication endpoint
@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username]['password'] == password:
        # Authentication successful, generate and return access token
        access_token = generate_access_token(username)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

# API endpoint for medical report generation 
@app.route('/medical-report', methods=['POST'])
def enqueue_report_generation():
    access_token = request.headers.get('Authorization')

    if validate_access_token(access_token):
        # authorization successful, enqueue report generation task
        data = request.json
        patient_id = data.get('patient_id')
        report_data = data.get('report_data')

        # enqueue report generation task
        report_queue.put({'patient_id': patient_id, 'report_data': report_data})

        return jsonify({'message': 'Report generation task queued successfully'}), 200
    else:
        return jsonify({'error': 'Unauthorized'}), 401

def generate_access_token(username):
    return "<randomly_generated_access_token>"

def validate_access_token(token):
    return token == "<randomly_generated_access_token>"

def generate_report(patient_id, report_data):
    print(f"Generating report for patient {patient_id} with data: {report_data}")

if __name__ == '__main__':
    app.run(debug=True)
