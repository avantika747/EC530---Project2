# implementing a sample REST API to process notifications with the help of queues

from flask import Flask, request, jsonify
from queue import Queue
from threading import Thread

app = Flask(__name__)

# initializing queue
notification_queue = Queue()

# worker function to process notifications (this notification_worker segment's idea borrowed from ChatGPT)
def notification_worker():
    while True:
        notification = notification_queue.get()
        if notification is None:
            break

        # processing notification
        send_notification(notification)
        notification_queue.task_done()

# starting the thread
notification_thread = Thread(target=notification_worker)
notification_thread.daemon = True
notification_thread.start()

# API endpoint to enqueue notifications
@app.route('/notifications', methods=['POST'])
def enqueue_notification():
    data = request.json
    notification_type = data.get('type')
    recipient = data.get('recipient')
    message = data.get('message')

    # enqueue notification
    notification_queue.put({'type': notification_type, 'recipient': recipient, 'message': message})

    return jsonify({'message': 'Notification queued successfully'}), 200

def send_notification(notification): 
    print(f"Sending {notification['type']} notification to {notification['recipient']}: {notification['message']}")

if __name__ == '__main__':
    app.run(debug=True)
