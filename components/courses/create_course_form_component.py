from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = page.get_by_test_id(
            'create-course-form-title-input'
        ).locator('input')
        self.create_course_estimated_time_input = page.get_by_test_id(
            'create-course-form-estimated-time-input'
        ).locator('input')
        self.create_course_description_textarea = (
            page.get_by_test_id('create-course-form-description-input')
            .locator('textarea')
            .first
        )
        self.create_course_max_score_input = page.get_by_test_id(
            'create-course-form-max-score-input'
        ).locator('input')
        self.create_course_min_score_input = page.get_by_test_id(
            'create-course-form-min-score-input'
        ).locator('input')

    def check_visible(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str,
    ):
        expect(self.create_course_title_input).to_be_visible()
        expect(self.create_course_title_input).to_have_value(title)

        expect(self.create_course_estimated_time_input).to_be_visible()
        expect(self.create_course_estimated_time_input).to_have_value(
            estimated_time
        )

        expect(self.create_course_description_textarea).to_be_visible()
        expect(self.create_course_description_textarea).to_have_value(
            description
        )

        expect(self.create_course_max_score_input).to_be_visible()
        expect(self.create_course_max_score_input).to_have_value(max_score)

        expect(self.create_course_min_score_input).to_be_visible()
        expect(self.create_course_min_score_input).to_have_value(min_score)

    def fill(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str,
    ):
        expect(self.create_course_title_input).to_be_visible()
        self.create_course_title_input.fill(title)

        expect(self.create_course_estimated_time_input).to_be_visible()
        self.create_course_estimated_time_input.fill(estimated_time)

        expect(self.create_course_description_textarea).to_be_visible()
        self.create_course_description_textarea.fill(description)

        expect(self.create_course_max_score_input).to_be_visible()
        self.create_course_max_score_input.fill(max_score)

        expect(self.create_course_min_score_input).to_be_visible()
        self.create_course_min_score_input.fill(min_score)
