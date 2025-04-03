import pytest

from pages.dashboard_page import DashboardPage


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
    )

    dashboard_page_with_state.sidebar.check_visible()
    dashboard_page_with_state.navbar.check_visible('username')

    dashboard_page_with_state.check_visible_dashboard_title()
    dashboard_page_with_state.check_visible_scores_chart()
    dashboard_page_with_state.check_visible_courses_chart()
    dashboard_page_with_state.check_visible_students_chart()
    dashboard_page_with_state.check_visible_activities_chart()
