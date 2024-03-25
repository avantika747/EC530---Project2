import pytest
import json
from flask import Flask
from API_report_generation_with_queue import app

@pytest.fixture
def client():
    # Create a test client using Flask's test_client method
    with app.test_client() as client:
        yield client
 
def test_login(client):
    # Define a sample login payload
    login_payload = {
        "username": "atticusfinch",
        "password": "justice"
        }
 
    # Make a POST request to the login endpoint
    response = client.post('/auth/login', json=login_payload)
     
    # Assert that the request was successful (status code 200)
    assert response.status_code == 200
 
    # Assert that the response contains the access token
    assert 'access_token' in response.json
 
def test_enqueue_report_generation(client):
    # Define a sample report generation payload
    report_payload = {
        "patient_id": "12345",
        "report_data": "Sample report data"
        }
 
    # Make a POST request to the report generation endpoint
    response = client.post('/medical-report', json=report_payload, headers={'Authorization': '<randomly_generated_access_token>'})
    
    # Assert that the request was successful (status code 200)
    assert response.status_code == 200

    # Assert that the response contains the expected message
    assert b'Report generation task queued successfully' in response.data


