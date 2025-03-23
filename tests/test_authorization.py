import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
    chromium_page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
    )

    chromium_page.get_by_test_id('login-form-email-input').locator(
        'input'
    ).fill('user.name@gmail.com')
    chromium_page.get_by_test_id('login-form-password-input').locator(
        'input'
    ).fill('password')
    chromium_page.get_by_test_id('login-page-login-button').click()

    alert_element = chromium_page.get_by_test_id(
        'login-page-wrong-email-or-password-alert'
    )
    expect(alert_element).to_be_visible()
    expect(alert_element).to_have_text('Wrong email or password')
