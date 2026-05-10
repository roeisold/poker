import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_security_headers(client):
    """Test that security headers are present in responses."""
    response = client.get('/')
    assert response.headers['X-Content-Type-Options'] == 'nosniff'
    assert response.headers['X-Frame-Options'] == 'SAMEORIGIN'
    assert response.headers['Referrer-Policy'] == 'strict-origin-when-cross-origin'
    assert 'Content-Security-Policy' in response.headers

def test_calculate_validation_root_dict(client):
    """Test that /calculate rejects non-dictionary roots."""
    response = client.post('/calculate', json=["not", "a", "dict"])
    assert response.status_code == 400
    assert response.json['error'] == "Invalid request: Expected JSON object"

def test_calculate_validation_friends_list(client):
    """Test that /calculate rejects non-list 'friends'."""
    response = client.post('/calculate', json={"friends": "not a list"})
    assert response.status_code == 400
    assert response.json['error'] == "Invalid request: 'friends' must be a list"

def test_calculate_validation_max_players(client):
    """Test that /calculate rejects more than 50 players."""
    friends = [[f"Player {i}", 0] for i in range(51)]
    response = client.post('/calculate', json={"friends": friends})
    assert response.status_code == 400
    assert response.json['error'] == "Invalid request: Maximum 50 players allowed"

def test_calculate_valid_request(client):
    """Test that a valid request still works."""
    data = {
        "friends": [["Alice", 0], ["Bob", 0]],
        "buy_ins": {"Alice": 10, "Bob": 10},
        "chip_counts": {"Alice": {"white": 40}, "Bob": {"white": 0}},
        "chip_values": {"white": 0.25},
        "selected_chips": ["white"]
    }
    response = client.post('/calculate', json=data)
    assert response.status_code == 200
    assert "transactions" in response.json
