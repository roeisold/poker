from playwright.sync_api import sync_playwright
import os
import time
import subprocess

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the app
        try:
            page.goto("http://127.0.0.1:5000")
        except Exception as e:
            print(f"Error navigating to page: {e}")
            return

        # The app might create 2 default players. Let's use those instead of adding more
        # and causing validation errors if empty.

        # Clear default players if necessary or just fill them
        players = page.query_selector_all(".friend-entry")
        if len(players) < 2:
            page.click("#addPlayerBtn")
            players = page.query_selector_all(".friend-entry")

        payload = "<img src=x onerror=window.xss_triggered=true>"

        # Fill first player
        players[0].query_selector(".friend-name").fill(payload)
        players[0].query_selector(".buy-in").fill("10")

        # Fill second player
        players[1].query_selector(".friend-name").fill("Bob")
        players[1].query_selector(".buy-in").fill("0")
        players[1].query_selector(".white-count").fill("100")

        # Click calculate
        page.click("button[type='submit']")

        # Wait for results to be populated
        try:
            page.wait_for_selector("#playersSummaryTable tr", state="visible", timeout=5000)
            print("Results table visible")
        except Exception as e:
            print(f"Results table not visible: {e}")
            page.screenshot(path="verification/timeout_error.png")

        # Check if XSS was triggered
        xss_triggered = page.evaluate("window.xss_triggered")
        print(f"XSS Triggered: {xss_triggered}")

        page.screenshot(path="verification/xss_repro.png")
        browser.close()

if __name__ == "__main__":
    # Ensure app is running
    process = subprocess.Popen(["python3", "app.py"])
    time.sleep(5)
    try:
        run_test()
    finally:
        process.kill()
