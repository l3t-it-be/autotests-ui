from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id(
            'registration-form-email-input'
        ).locator('input')
        self.username_input = page.get_by_test_id(
            'registration-form-username-input'
        ).locator('input')
        self.password_input = page.get_by_test_id(
            'registration-form-password-input'
        ).locator('input')

    def fill(self, email: str, username: str, password: str):
        expect(self.email_input).to_be_visible()
        self.email_input.fill(email)

        expect(self.username_input).to_be_visible()
        self.username_input.fill(username)

        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)

    def check_visible(self, email, username, password):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.username_input).to_be_visible()
        expect(self.username_input).to_have_value(username)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)
