from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_email_input = page.get_by_test_id(
            'registration-form-email-input'
        ).locator('input')
        self.registration_username_input = page.get_by_test_id(
            'registration-form-username-input'
        ).locator('input')
        self.registration_password_input = page.get_by_test_id(
            'registration-form-password-input'
        ).locator('input')
        self.registration_button = page.get_by_test_id(
            'registration-page-registration-button'
        )

    def fill_registration_form(self, email: str, username: str, password: str):
        self.registration_email_input.fill(email)
        expect(self.registration_email_input).to_have_value(email)

        self.registration_username_input.fill(username)
        expect(self.registration_username_input).to_have_value(username)

        self.registration_password_input.fill(password)
        expect(self.registration_password_input).to_have_value(password)

    def click_registration_button(self):
        self.registration_button.click()
