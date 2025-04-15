import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title = Text(
            page, 'Dashboard title', 'dashboard-toolbar-title-text'
        )

    @allure.step('Check visible dashboard title')
    def check_visible(self):
        self.dashboard_title.check_visible()
        self.dashboard_title.check_have_text('Dashboard')
