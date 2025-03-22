import os

import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        )

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

        registration_button = page.get_by_test_id(
            'registration-page-registration-button'
        )
        registration_button.click()

        dashboard_page_title = page.get_by_test_id(
            'dashboard-toolbar-title-text'
        )
        expect(dashboard_page_title).to_be_visible()
        expect(dashboard_page_title).to_have_text('Dashboard')

        storage_state_path = os.path.abspath('../browser-state.json')
        context.storage_state(path=storage_state_path)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state=storage_state_path)
        page = context.new_page()

        page.goto(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
        )

        courses_page_title = page.get_by_test_id(
            'courses-list-toolbar-title-text'
        )
        expect(courses_page_title).to_be_visible()
        expect(courses_page_title).to_have_text('Courses')

        empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_view_icon).to_be_visible()

        empty_view_title = page.get_by_test_id(
            'courses-list-empty-view-title-text'
        )
        expect(empty_view_title).to_be_visible()
        expect(empty_view_title).to_have_text('There is no results')

        empty_view_description = page.get_by_test_id(
            'courses-list-empty-view-description-text'
        )
        expect(empty_view_description).to_be_visible()
        expect(empty_view_description).to_have_text(
            'Results from the load test pipeline will be displayed here'
        )
