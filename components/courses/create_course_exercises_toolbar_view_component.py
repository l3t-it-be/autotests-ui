from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_title = Text(
            page,
            'Exercises title',
            'create-course-exercises-box-toolbar-title-text',
        )
        self.create_exercise_button = Button(
            page,
            'Create exercise',
            'create-course-exercises-box-toolbar-create-exercise-button',
        )

    def check_visible(self):
        self.exercises_title.check_visible()
        self.exercises_title.check_have_text('Exercises')

        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()
