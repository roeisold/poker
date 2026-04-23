from playwright.sync_api import sync_playwright
import os
import time
import subprocess
import json

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Testing index.html XSS fix...")
        try:
            page.goto("http://127.0.0.1:5000")
            # Inject malicious playerData into localStorage
            payload = '"><img src=x onerror=window.xss_triggered=true>'
            player_data = [
                {
                    "name": "Hacker",
                    "buyIn": "10",
                    "chipCounts": {
                        "white": payload
                    }
                }
            ]
            page.evaluate(f"localStorage.setItem('playerData', '{json.dumps(player_data)}')")
            page.reload()
            time.sleep(2)
            xss_triggered = page.evaluate("window.xss_triggered")
            if xss_triggered:
                print("FAILED: XSS triggered in index.html")
                return False
            else:
                print("PASSED: XSS not triggered in index.html")
        except Exception as e:
            print(f"Error testing index.html: {e}")
            return False

        print("Testing chip_setup.html XSS fix...")
        try:
            page.goto("http://127.0.0.1:5000/chip-setup")
            # Inject malicious chipValues into localStorage
            payload = '"><img src=x onerror=window.xss_triggered=true>'
            chip_values = {
                "white": payload
            }
            page.evaluate(f"localStorage.setItem('chipValues', '{json.dumps(chip_values)}')")
            page.reload()
            time.sleep(2)
            xss_triggered = page.evaluate("window.xss_triggered")
            if xss_triggered:
                print("FAILED: XSS triggered in chip_setup.html")
                return False
            else:
                print("PASSED: XSS not triggered in chip_setup.html")
        except Exception as e:
            print(f"Error testing chip_setup.html: {e}")
            return False

        browser.close()
        return True

if __name__ == "__main__":
    process = subprocess.Popen(["python3", "app.py"])
    time.sleep(3)
    success = False
    try:
        success = run_test()
    finally:
        process.kill()

    if not success:
        exit(1)
