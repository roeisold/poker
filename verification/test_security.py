import requests
import pytest
import subprocess
import time

BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture(scope="session", autouse=True)
def server():
    # Start the server
    process = subprocess.Popen(["python3", "app.py"])
    time.sleep(2)  # Give the server time to start
    yield
    # Kill the server
    process.terminate()
    process.wait()

def test_security_headers():
    response = requests.get(BASE_URL)
    assert response.headers['X-Content-Type-Options'] == 'nosniff'
    assert response.headers['X-Frame-Options'] == 'SAMEORIGIN'
    assert response.headers['Referrer-Policy'] == 'strict-origin-when-cross-origin'
    assert 'Content-Security-Policy' in response.headers

def test_calculate_player_limit():
    # 51 players
    friends = [[f"Player{i}", 0] for i in range(51)]
    payload = {
        "friends": friends,
        "buy_ins": {},
        "chip_counts": {}
    }
    response = requests.post(f"{BASE_URL}/calculate", json=payload)
    assert response.status_code == 400
    assert "Maximum 50 players allowed" in response.json()['error']

def test_calculate_invalid_json_type():
    # Send a list instead of an object
    response = requests.post(f"{BASE_URL}/calculate", json=[1, 2, 3])
    assert response.status_code == 400
    assert "Expected JSON object" in response.json()['error']

def test_calculate_invalid_friends_type():
    payload = {
        "friends": "not a list",
        "buy_ins": {},
        "chip_counts": {}
    }
    response = requests.post(f"{BASE_URL}/calculate", json=payload)
    assert response.status_code == 400
    assert "'friends' must be a list" in response.json()['error']
