import requests
import time
import subprocess
import os

def test_security():
    # Start the server
    process = subprocess.Popen(["python3", "app.py"])
    time.sleep(2)

    base_url = "http://127.0.0.1:5000"

    try:
        # 1. Test Security Headers
        print("Testing security headers...")
        r = requests.get(base_url)
        headers = r.headers

        assert "Content-Security-Policy" in headers
        csp = headers["Content-Security-Policy"]
        assert "base-uri 'none'" in csp
        assert "form-action 'self'" in csp

        assert headers.get("X-Content-Type-Options") == "nosniff"
        assert headers.get("X-Frame-Options") == "SAMEORIGIN"
        assert headers.get("Referrer-Policy") == "strict-origin-when-cross-origin"
        print("✅ Security headers passed.")

        # 2. Test Input Validation - Non-JSON
        print("Testing non-JSON payload...")
        r = requests.post(f"{base_url}/calculate", data="not a json")
        assert r.status_code == 400
        assert r.json().get("error") == "Invalid request: Payload must be a JSON object"
        print("✅ Non-JSON payload validation passed.")

        # 3. Test Input Validation - Missing/Invalid friends
        print("Testing invalid friends list...")
        r = requests.post(f"{base_url}/calculate", json={"friends": "not a list"})
        assert r.status_code == 400
        assert "friends' must be a list" in r.json().get("error")
        print("✅ Invalid friends list validation passed.")

        # 4. Test Input Validation - Player Limit
        print("Testing player limit...")
        r = requests.post(f"{base_url}/calculate", json={"friends": [["P" + str(i), 0] for i in range(51)]})
        assert r.status_code == 400
        assert "Player limit of 50 exceeded" in r.json().get("error")
        print("✅ Player limit validation passed.")

        # 5. Test Input Validation - Malformed friends entry
        print("Testing malformed friends entry...")
        r = requests.post(f"{base_url}/calculate", json={"friends": [["Alice"]]}) # Length 1 instead of 2
        assert r.status_code == 400
        assert "Malformed friends list" in r.json().get("error")
        print("✅ Malformed friends entry validation passed.")

        # 6. Test Input Validation - Duplicate Names
        print("Testing duplicate names...")
        r = requests.post(f"{base_url}/calculate", json={"friends": [["Alice", 0], ["alice", 0]]})
        assert r.status_code == 400
        assert "Duplicate player names detected" in r.json().get("error")
        print("✅ Duplicate names validation passed.")

        # 7. Test Input Validation - Malformed players data
        print("Testing malformed players data...")
        r = requests.post(f"{base_url}/calculate", json={"friends": [["Alice", 0]], "buy_ins": ["not a dict"]})
        assert r.status_code == 400
        assert "Malformed players data" in r.json().get("error")
        print("✅ Malformed players data validation passed.")

        # 8. Test Input Validation - Malformed chip settings
        print("Testing malformed chip settings...")
        r = requests.post(f"{base_url}/calculate", json={"friends": [["Alice", 0]], "chip_values": "not a dict"})
        assert r.status_code == 400
        assert "Malformed chip settings" in r.json().get("error")
        print("✅ Malformed chip settings validation passed.")

        # 9. Test Valid Calculation
        print("Testing valid calculation...")
        valid_payload = {
            "friends": [["Alice", 0], ["Bob", 0]],
            "buy_ins": {"Alice": 10, "Bob": 0},
            "chip_counts": {"Alice": {}, "Bob": {"white": 40}},
            "chip_values": {"white": 0.25},
            "selected_chips": ["white"]
        }
        r = requests.post(f"{base_url}/calculate", json=valid_payload)
        assert r.status_code == 200
        data = r.json()
        assert len(data["transactions"]) == 1
        assert data["transactions"][0]["payer"] == "Alice"
        assert data["transactions"][0]["receiver"] == "Bob"
        assert data["transactions"][0]["amount"] == 10.0
        print("✅ Valid calculation passed.")

    finally:
        process.kill()

if __name__ == "__main__":
    try:
        test_security()
        print("\nALL SECURITY AND VALIDATION TESTS PASSED!")
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        exit(1)
