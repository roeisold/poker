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

        # Add a player with an XSS payload in the name
        # We need to find the first player name input
        payload = "<img src=x onerror=window.xss_triggered=true>"
        page.fill(".friend-name", payload)
        page.fill(".buy-in", "10")

        # Add another player so we have a transaction
        page.click("#addPlayerBtn")
        # Wait a bit for the new player entry to appear
        page.wait_for_selector(".friend-entry:nth-child(2)")
        page.fill(".friend-entry:nth-child(2) .friend-name", "Bob")
        page.fill(".friend-entry:nth-child(2) .buy-in", "0")

        # Give Bob some chips so he's a creditor or debtor
        # In this case, payer = me (10 buy in, 0 chips), receiver = Bob (0 buy in, some chips)
        # Wait, let's just make sure Bob has chips.
        # Find the first chip input for Bob
        page.fill(".friend-entry:nth-child(2) .white-count", "100") # 100 * 0.25 = 25

        # Click calculate
        page.click("button[type='submit']")

        # Wait for results or timeout
        try:
            page.wait_for_selector("#resultsCard", state="visible", timeout=5000)
        except:
            print("Results card did not appear (this might be expected if payload broke JS or if we just want to check XSS)")

        # Check if XSS was triggered
        xss_triggered = page.evaluate("window.xss_triggered")
        print(f"XSS Triggered: {xss_triggered}")

        if xss_triggered:
             print("FAILURE: XSS was triggered!")
        else:
             print("SUCCESS: XSS was NOT triggered.")

        page.screenshot(path="verification/xss_repro.png")
        browser.close()

if __name__ == "__main__":
    # Ensure app is running
    # The previous run_in_bash_session might have failed to keep it running
    # or it might still be running. Let's try to start it and wait.
    process = subprocess.Popen(["python3", "app.py"])
    time.sleep(3)
    try:
        run_test()
    finally:
        process.kill()
