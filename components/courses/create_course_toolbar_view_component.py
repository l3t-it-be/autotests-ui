import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(
            page,
            'Create course title',
            'create-course-toolbar-title-text',
        )
        self.create_course_button = Button(
            page, 'Create course', 'create-course-toolbar-create-course-button'
        )

    @allure.step('Check visible create course toolbar')
    def check_visible(self, is_create_course_disabled=True):
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')

        self.create_course_button.check_visible()
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()
