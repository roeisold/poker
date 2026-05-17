import requests
import json
import time
import subprocess

def test_validation():
    url = "http://127.0.0.1:5000/calculate"

    # 1. Test malformed JSON (not an object)
    print("Testing malformed JSON (not an object)...")
    resp = requests.post(url, data="[1,2,3]", headers={"Content-Type": "application/json"})
    assert resp.status_code == 400
    assert resp.json()["error"] == "Invalid request: Payload must be a JSON object"
    print("  PASSED")

    # 2. Test player limit
    print("Testing player limit (51 players)...")
    payload = {
        "friends": [[f"Player{i}", 0] for i in range(51)],
        "buy_ins": {},
        "chip_counts": {}
    }
    resp = requests.post(url, json=payload)
    assert resp.status_code == 400
    assert resp.json()["error"] == "Invalid request: Player limit of 50 exceeded"
    print("  PASSED")

    # 3. Test duplicate names
    print("Testing duplicate names...")
    payload = {
        "friends": [["Alice", 0], ["alice", 0]],
        "buy_ins": {},
        "chip_counts": {}
    }
    resp = requests.post(url, json=payload)
    assert resp.status_code == 400
    assert "Duplicate name" in resp.json()["error"]
    print("  PASSED")

    # 4. Test malformed players data
    print("Testing malformed players data (friends not a list)...")
    payload = {
        "friends": "not a list",
        "buy_ins": {},
        "chip_counts": {}
    }
    resp = requests.post(url, json=payload)
    assert resp.status_code == 400
    assert "Malformed players data" in resp.json()["error"]
    print("  PASSED")

    # 5. Test valid calculation still works
    print("Testing valid calculation...")
    payload = {
        "friends": [["Alice", 0], ["Bob", 0]],
        "buy_ins": {"Alice": 10, "Bob": 0},
        "chip_counts": {"Alice": {"white": 0}, "Bob": {"white": 10}},
        "chip_values": {"white": 1},
        "selected_chips": ["white"]
    }
    # Wait, the app uses DEFAULT_CHIP_VALUES if not provided.
    # If I give Alice 10 buy in and 0 chips, she is -10.
    # If Bob has 0 buy in and 10 white chips (value 1), he is +10.
    # Total imbalance 0.
    # Alice pays Bob 10.
    resp = requests.post(url, json=payload)
    if resp.status_code != 200:
        print(f"  FAILED: {resp.status_code} {resp.text}")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["transactions"]) == 1
    assert data["transactions"][0]["payer"] == "Alice"
    assert data["transactions"][0]["receiver"] == "Bob"
    assert data["transactions"][0]["amount"] == 10
    print("  PASSED")

if __name__ == "__main__":
    process = subprocess.Popen(["python3", "app.py"])
    time.sleep(3)
    try:
        test_validation()
        print("\nALL VALIDATION TESTS PASSED")
    finally:
        process.kill()
