import allure
from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return 'input'

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(
            f'Fill {self.type_of} "{self.name}" with value "{value}"'
        ):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(
            f'Checking that {self.type_of} "{self.name}" has value "{value}"'
        ):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)
