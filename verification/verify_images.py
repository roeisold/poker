from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    page.goto("http://localhost:5000")
    page.wait_for_timeout(1000)

    # Take screenshot of home page
    page.screenshot(path="/home/jules/verification/screenshots/index.png")

    # Go to chip setup
    page.get_by_role("link", name="⚙️ Setup Chip Values").click()
    page.wait_for_timeout(1000)

    # Take screenshot of chip setup page
    page.screenshot(path="/home/jules/verification/screenshots/chip_setup.png")

    # Go back to home
    page.get_by_role("link", name="Cancel").click()
    page.wait_for_timeout(1000)

    # Enter some player data
    player_names = page.query_selector_all(".friend-name")
    if len(player_names) >= 1:
        player_names[0].fill("Alice")
        page.wait_for_timeout(500)

    # Click calculate
    page.get_by_role("button", name="Calculate Debts").click()
    page.wait_for_timeout(2000)

    # Final screenshot
    page.screenshot(path="/home/jules/verification/screenshots/final.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
