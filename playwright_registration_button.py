from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
    )

    registration_button = page.get_by_test_id(
        'registration-page-registration-button'
    )
    expect(registration_button).to_be_disabled()

    registration_email_input = page.get_by_test_id(
        'registration-form-email-input'
    ).locator('input')
    registration_email_input.fill('user.name@gmail.com')

    registration_username_input = page.get_by_test_id(
        'registration-form-username-input'
    ).locator('input')
    registration_username_input.fill('username')

    registration_password_input = page.get_by_test_id(
        'registration-form-password-input'
    ).locator('input')
    registration_password_input.fill('password')

    expect(registration_button).to_be_enabled()
