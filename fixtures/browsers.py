import os
from typing import Generator, Any

import pytest
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

storage_state_path = os.path.abspath('../browser-state.json')


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
    )

    registration_page.registration_form.fill(
        email='user.name@gmail.com', username='username', password='password'
    )
    registration_page.click_registration_button()

    dashboard_page = DashboardPage(page)
    dashboard_page.dashboard_toolbar.check_visible()

    context.storage_state(path=storage_state_path)
    browser.close()


@pytest.fixture()
def chromium_page_with_state(playwright: Playwright, initialize_browser_state):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=storage_state_path)
    page = context.new_page()

    yield page
    browser.close()
