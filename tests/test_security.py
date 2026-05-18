import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_security_headers(client):
    response = client.get('/')
    assert response.headers['Content-Security-Policy'] == (
        "default-src 'self'; "
        "script-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
        "style-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
        "img-src 'self' data:; "
        "base-uri 'none'; "
        "form-action 'self';"
    )
    assert response.headers['X-Content-Type-Options'] == 'nosniff'
    assert response.headers['X-Frame-Options'] == 'SAMEORIGIN'
    assert response.headers['Referrer-Policy'] == 'strict-origin-when-cross-origin'

def test_duplicate_names(client):
    payload = {
        "friends": [["Alice", 0], ["alice", 0]],
        "buy_ins": {"Alice": 10, "alice": 10},
        "chip_counts": {"Alice": {}, "alice": {}}
    }
    response = client.post('/calculate', json=payload)
    assert response.status_code == 400
    assert response.get_json()['error'] == "Invalid request: Duplicate player names detected"

def test_player_limit(client):
    payload = {
        "friends": [[f"p{i}", 0] for i in range(51)]
    }
    response = client.post('/calculate', json=payload)
    assert response.status_code == 400
    assert response.get_json()['error'] == "Invalid request: Player limit of 50 exceeded"

def test_malformed_json(client):
    response = client.post('/calculate', data="not json", content_type='application/json')
    assert response.status_code == 400
    assert response.get_json()['error'] == "Invalid request: Payload must be a JSON object"

def test_friends_type_check(client):
    payload = {"friends": "not a list"}
    response = client.post('/calculate', json=payload)
    assert response.status_code == 400
    assert response.get_json()['error'] == "Invalid request: 'friends' must be a list"
