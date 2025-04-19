import re

from playwright.sync_api import Page

from components.authentication.registration_form_component import (
    RegistrationFormComponent,
)
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(self.page)

        self.registration_button = Button(
            page,
            'Registration',
            'registration-page-registration-button',
        )
        self.login_link = Link(page, 'Login', 'registration-page-login-link')

    def click_registration_button(self):
        self.registration_button.click()
        self.check_current_url(re.compile('./#/dashboard'))
