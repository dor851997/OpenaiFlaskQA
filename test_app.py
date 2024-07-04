import pytest
from flask import Flask
from app import app as flask_app

@pytest.fixture
def app():
    # Set up the Flask app with a testing configuration
    flask_app.config.update({
        "TESTING": True,
    })

    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_ask_endpoint(client):
    # Send a POST request to the /ask endpoint
    response = client.post("/ask", data={"promptmsg": "What is AI?"})

    # Ensure the request was successful
    assert response.status_code == 302  # Redirect status

    # Follow the redirect to get the final response
    follow_response = client.get(response.headers["Location"])

    # Ensure the final response was successful
    assert follow_response.status_code == 200

    # Check if the response data contains the expected result
    assert b'What is AI?' in follow_response.data
