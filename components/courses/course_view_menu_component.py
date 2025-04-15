import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'Menu', 'course-view-menu-button')
        self.edit_menu_item = Button(
            page, 'Edit', 'course-view-edit-menu-item'
        )
        self.delete_menu_item = Button(
            page, 'Delete', 'course-view-delete-menu-item'
        )

    @allure.step('Open menu of the course with index "{index}" and click edit')
    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_item.check_visible(nth=index)
        self.edit_menu_item.click(nth=index)

    @allure.step(
        'Open menu of the course with index "{index}" and click delete'
    )
    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_item.check_visible(nth=index)
        self.delete_menu_item.click(nth=index)
