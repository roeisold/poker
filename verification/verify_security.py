import requests
import subprocess
import time
import os

def test_security():
    print("Starting app...")
    process = subprocess.Popen(["python3", "app.py"])
    time.sleep(2)

    try:
        # Test Headers
        print("\nChecking Headers...")
        r = requests.get('http://127.0.0.1:5000/')
        headers = r.headers
        for h in ['Content-Security-Policy', 'X-Content-Type-Options', 'X-Frame-Options', 'Referrer-Policy']:
            if h in headers:
                print(f"✅ {h}: {headers[h]}")
            else:
                print(f"❌ {h} is MISSING")

        # Test Calculation Limit
        print("\nChecking Player Limit...")
        url = 'http://127.0.0.1:5000/calculate'
        # Send 51 players
        payload = {
            'friends': [['Player' + str(i), 0] for i in range(51)],
            'buy_ins': {},
            'chip_counts': {},
            'chip_values': {},
            'selected_chips': []
        }
        r = requests.post(url, json=payload)
        print(f"Response Code for 51 players: {r.status_code}")
        print(f"Response Body: {r.text}")

        # Test non-dict JSON
        print("\nChecking non-dict JSON...")
        r = requests.post(url, json=[1, 2, 3])
        print(f"Response Code for list JSON: {r.status_code}")
        print(f"Response Body: {r.text}")

        # Test escapeHTML with 0 (manual check via script execution logic if it was JS,
        # but here we just note it for the fix)

    finally:
        print("\nStopping app...")
        process.kill()

if __name__ == "__main__":
    test_security()
