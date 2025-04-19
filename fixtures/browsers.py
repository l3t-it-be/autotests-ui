from typing import Generator, Any

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from config import settings
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.playwright.pages import initialize_playwright_page
from tools.roots import AppRoute


@pytest.fixture
def chromium_page(
    request: SubRequest, playwright: Playwright
) -> Generator[Page, Any, None]:
    yield from initialize_playwright_page(
        playwright, test_name=request.node.name
    )


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit(AppRoute.REGISTRATION)

    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password,
    )
    registration_page.click_registration_button()

    dashboard_page = DashboardPage(page)
    dashboard_page.dashboard_toolbar.check_visible()

    context.storage_state(path=settings.browser_state_file)
    browser.close()


@pytest.fixture()
def chromium_page_with_state(
    initialize_browser_state, request: SubRequest, playwright: Playwright
):
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file,
    )
