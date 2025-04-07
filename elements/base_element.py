from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, name: str, locator: str):
        self.page = page
        self.name = name
        self.locator = locator

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator)

    def click(self, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.click()

    def check_visible(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)
