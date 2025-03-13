from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
        wait_until='networkidle',
    )

    page.evaluate(
        """
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """
    )
    page.wait_for_timeout(2000)
