import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(
            page, 'Courses toolbar title', 'courses-list-toolbar-title-text'
        )
        self.create_course_button = Button(
            page, 'Create course', 'courses-list-toolbar-create-course-button'
        )

    @allure.step(
        'Check visible courses list toolbar title and create course button'
    )
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Courses')

        self.create_course_button.check_visible()

    @allure.step('')
    def click_create_course_button(self):
        self.create_course_button.click()
        self.check_current_url(re.compile('.*/#/courses/create'))
