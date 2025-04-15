import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page, 'Title', f'{identifier}-widget-title-text')
        self.chart = Image(page, 'Chart', f'{identifier}-{chart_type}-chart')

    @allure.step('Check visible chart view "{text}"')
    def check_visible(self, text: str):
        self.title.check_visible()
        self.title.check_have_text(text)
        self.chart.check_visible()
