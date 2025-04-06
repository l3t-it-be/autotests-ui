from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title = page.get_by_test_id(
            'dashboard-toolbar-title-text'
        )

    def check_visible(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text('Dashboard')
