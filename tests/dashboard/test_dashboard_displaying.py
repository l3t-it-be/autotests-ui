import allure
import pytest
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(
        self, dashboard_page_with_state: DashboardPage
    ):
        dashboard_page_with_state.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
        )

        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible('username')

        dashboard_page_with_state.dashboard_toolbar.check_visible()

        dashboard_page_with_state.students_chart_view.check_visible('Students')
        dashboard_page_with_state.activities_chart_view.check_visible(
            'Activities'
        )
        dashboard_page_with_state.courses_chart_view.check_visible('Courses')
        dashboard_page_with_state.scores_chart_view.check_visible('Scores')
