import pytest

from pages.login_page import LoginPage

credentials = {
    'invalid_email_and_password': ('user.name@gmail.com', 'password'),
    'invalid_email_and_empty_password': ('user.name@gmail.com', '  '),
    'empty_email_and_invalid_password': ('  ', 'password'),
}


@pytest.mark.parametrize(
    'email, password', credentials.values(), ids=credentials.keys()
)
@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(
    login_page: LoginPage, email: str, password: str
):
    login_page.visit(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
    )
    login_page.login_form.fill(email, password)
    login_page.login_form.check_visible(email, password)
    login_page.click_login_button()

    login_page.check_visible_wrong_email_or_password_alert()
