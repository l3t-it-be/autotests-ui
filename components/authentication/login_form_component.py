from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'Login email', 'login-form-email-input')
        self.password_input = Input(
            page, 'Login password', 'login-form-password-input'
        )

    def fill(self, email: str, password: str):
        self.email_input.check_visible()
        self.email_input.fill(email)

        self.password_input.check_visible()
        self.password_input.fill(password)

    def check_visible(self, email, password):
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)
