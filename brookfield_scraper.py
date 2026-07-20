from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://www.brookfield.com/about-us/leadership",
        timeout=120000
    )

    page.wait_for_timeout(5000)

    page.locator("a").nth(161).click()

    page.wait_for_timeout(5000)

    print(page.url)

    print("\nFIRST 1000 CHARS:\n")
    print(page.locator("body").inner_text()[:1000])

    input("Press Enter...")