import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return 'file input'

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        with allure.step(
            f'Choose file "{file}" for {self.type_of} "{self.name}"'
        ):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
