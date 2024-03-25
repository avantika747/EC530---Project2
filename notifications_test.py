import pytest
import json
from flask import Flask
from API_notifications_with_queue import app, send_notification

@pytest.fixture
def client():
    # Create a test client using Flask's test_client method
    with app.test_client() as client:
        yield client
 
def test_enqueue_notification(client):
    # Define a sample notification payload
    notification_payload = {
        "type": "email",
        "recipient": "test@example.com",
        "message": "This is a test notification."
        }
 
    # Make a POST request to enqueue a notification
    response = client.post('/notifications', json=notification_payload)
     
    # Assert that the request was successful (status code 200)
    assert response.status_code == 200
 
    # Assert that the response contains the expected message
    assert b'Notification queued successfully' in response.data
 
def test_send_notification():
    # Define a sample notification
    notification = {
        "type": "email",
        "recipient": "test@example.com",
        "message": "This is a test notification."
        }
 
    # Call the send_notification function
    result = send_notification(notification)

    # Assert that the result is True (notification sent successfully)
    assert result == True

