import requests

def test_calculate_validation():
    url = "http://127.0.0.1:5000/calculate"

    print("Testing with non-JSON body...")
    try:
        response = requests.post(url, data="not a json", headers={"Content-Type": "application/json"})
        print(f"Status: {response.status_code}, Body: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

    print("\nTesting with huge number of players...")
    huge_friends = [["Player" + str(i), 0] for i in range(1000)]
    try:
        response = requests.post(url, json={"friends": huge_friends})
        print(f"Status: {response.status_code}, Body: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

def test_security_headers():
    url = "http://127.0.0.1:5000/"
    print("\nTesting security headers...")
    try:
        response = requests.get(url)
        headers = response.headers
        for header in ['Content-Security-Policy', 'X-Content-Type-Options', 'X-Frame-Options', 'Referrer-Policy']:
            print(f"{header}: {headers.get(header, 'MISSING')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_calculate_validation()
    test_security_headers()
