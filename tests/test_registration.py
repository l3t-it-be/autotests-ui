import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
    )

    registration_email_input = chromium_page.get_by_test_id(
        'registration-form-email-input'
    ).locator('input')
    registration_email_input.fill('user.name@gmail.com')

    registration_username_input = chromium_page.get_by_test_id(
        'registration-form-username-input'
    ).locator('input')
    registration_username_input.fill('username')

    registration_password_input = chromium_page.get_by_test_id(
        'registration-form-password-input'
    ).locator('input')
    registration_password_input.fill('password')

    registration_button = chromium_page.get_by_test_id(
        'registration-page-registration-button'
    )
    registration_button.click()

    dashboard_page_title = chromium_page.get_by_test_id(
        'dashboard-toolbar-title-text'
    )
    expect(dashboard_page_title).to_be_visible()
    expect(dashboard_page_title).to_have_text('Dashboard')
