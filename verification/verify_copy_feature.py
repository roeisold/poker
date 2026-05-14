import subprocess
import time
from playwright.sync_api import sync_playwright

def run_verification():
    # Start the Flask app
    proc = subprocess.Popen(['python3', 'app.py'])
    time.sleep(2)  # Wait for server to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                permissions=['clipboard-read', 'clipboard-write']
            )
            page = context.new_page()
            page.goto('http://127.0.0.1:5000')

            # Fill in some player data
            # Default has 2 players
            page.locator('.friend-name').nth(0).fill('Alice')
            page.locator('.buy-in').nth(0).fill('100')
            page.locator('.white-count').nth(0).fill('400') # 400 * 0.25 = 100, Alice is even

            page.locator('.friend-name').nth(1).fill('Bob')
            page.locator('.buy-in').nth(1).fill('50')
            page.locator('.white-count').nth(1).fill('0') # Bob owes 50

            # Add Charlie who won 50
            page.click('#addPlayerBtn')
            page.locator('.friend-name').nth(2).fill('Charlie')
            page.locator('.buy-in').nth(2).fill('0')
            page.locator('.white-count').nth(2).fill('200') # 200 * 0.25 = 50

            # Calculate
            page.click('button[type="submit"]')

            # Wait for results
            page.wait_for_selector('#resultsCard', state='visible')

            # Verify Copy button is visible
            copy_btn = page.locator('#copyBtn')
            if not copy_btn.is_visible():
                raise Exception("Copy button not visible after calculation")

            print("Copy button is visible.")

            # Click copy button
            copy_btn.click()

            # Verify feedback text
            page.wait_for_selector('text=✓ Copied!', timeout=5000)
            print("Visual feedback '✓ Copied!' verified.")

            # Check if button reverts after 2 seconds
            time.sleep(2.5)
            if "📋 Copy Settlement Plan" not in copy_btn.inner_text():
                raise Exception(f"Button text did not revert. Current text: {copy_btn.inner_text()}")

            print("Button text reverted successfully.")

            # Verify accessibility attributes
            if copy_btn.get_attribute('title') != "Copy settlement plan to clipboard":
                raise Exception("Copy button missing correct title")

            print("Accessibility attributes verified.")

            browser.close()
            print("Verification successful!")

    finally:
        proc.terminate()

if __name__ == "__main__":
    run_verification()
