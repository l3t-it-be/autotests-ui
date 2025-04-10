from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = Input(
            page, 'Course title', 'create-course-form-title-input'
        )
        self.create_course_estimated_time_input = Input(
            page,
            'Course estimated time',
            'create-course-form-estimated-time-input',
        )
        self.create_course_description_textarea = Textarea(
            page, 'Course description', 'create-course-form-description-input'
        )
        self.create_course_max_score_input = Input(
            page, 'Course max score', 'create-course-form-max-score-input'
        )
        self.create_course_min_score_input = Input(
            page, 'Course min score', 'create-course-form-min-score-input'
        )

    def check_visible(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str,
    ):
        self.create_course_title_input.check_visible()
        self.create_course_title_input.check_have_value(title)

        self.create_course_estimated_time_input.check_visible()
        self.create_course_estimated_time_input.check_have_value(
            estimated_time
        )

        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.check_have_value(description)

        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.check_have_value(max_score)

        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.check_have_value(min_score)

    def fill(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str,
    ):
        self.create_course_title_input.check_visible()
        self.create_course_title_input.fill(title)

        self.create_course_estimated_time_input.check_visible()
        self.create_course_estimated_time_input.fill(estimated_time)

        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.fill(description)

        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.fill(max_score)

        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.fill(min_score)
