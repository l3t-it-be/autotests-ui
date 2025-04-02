from playwright.sync_api import expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.page_title = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_dashboard_page_title_visibility(self):
        expect(self.page_title).to_be_visible()
        expect(self.page_title).to_have_text('Dashboard')
