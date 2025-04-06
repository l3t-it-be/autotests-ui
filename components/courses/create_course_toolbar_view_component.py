from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = page.get_by_test_id(
            'create-course-toolbar-title-text'
        )
        self.create_course_button = page.get_by_test_id(
            'create-course-toolbar-create-course-button'
        )

    def check_visible(self, is_create_course_disabled=True):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

        expect(self.create_course_button).to_be_visible()
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()
        else:
            expect(self.create_course_button).to_be_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()
