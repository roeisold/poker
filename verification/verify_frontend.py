import subprocess
import time
from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto('http://127.0.0.1:5000')
    page.wait_for_timeout(500)

    # 1. Add some players and calculate
    page.locator('.friend-name').nth(0).fill('Alice')
    page.wait_for_timeout(500)
    page.locator('.buy-in').nth(0).fill('100')
    page.wait_for_timeout(500)

    page.locator('.friend-name').nth(1).fill('Bob')
    page.wait_for_timeout(500)
    page.locator('.buy-in').nth(1).fill('50')
    page.wait_for_timeout(500)
    page.locator('.white-count').nth(1).fill('200') # Bob is even (50 - 50)
    page.wait_for_timeout(500)

    # Add Charlie who owes Alice
    page.click('#addPlayerBtn')
    page.wait_for_timeout(500)
    page.locator('.friend-name').nth(2).fill('Charlie')
    page.wait_for_timeout(500)
    page.locator('.buy-in').nth(2).fill('0')
    page.wait_for_timeout(500)
    page.locator('.white-count').nth(2).fill('0') # Charlie owes 100 / 3 roughly?
    # Actually let's make it simple
    # Alice buy 100, chips 150 -> Alice +50
    # Bob buy 50, chips 50 -> Bob 0
    # Charlie buy 0, chips 0 -> Charlie 0
    # Total buy 150, total chips 200 -> Imbalance +50

    # Let's just calculate
    page.click('button[type="submit"]')
    page.wait_for_timeout(1000)

    # 2. Verify results and copy button
    page.wait_for_selector('#resultsCard', state='visible')
    page.wait_for_timeout(500)

    page.screenshot(path="/home/jules/verification/screenshots/results_with_copy.png")
    page.wait_for_timeout(500)

    # 3. Click Copy button
    page.click('#copyBtn')
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/copied_feedback.png")

    # 4. Go to Chip Setup
    page.click('text=⚙️ Setup Chip Values')
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/chip_setup_a11y.png")
    page.wait_for_timeout(500)

    page.wait_for_timeout(1000)  # Hold final state for the video

if __name__ == "__main__":
    # Start the Flask app
    proc = subprocess.Popen(['python3', 'app.py'])
    time.sleep(2)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                record_video_dir="/home/jules/verification/videos"
            )
            page = context.new_page()
            run_cuj(page)
            context.close()
            browser.close()
    finally:
        proc.terminate()
