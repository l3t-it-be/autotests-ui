import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print('[AUTOUSE] Отправляем данные в сервис аналитики')


@pytest.fixture(scope='session')
def settings():
    print('[SESSION] Инициализируем настройки автотестов')


@pytest.fixture(scope='class')
def user():
    print('[CLASS] Создаем данные пользователя один раз на тестовый класс')


@pytest.fixture(scope='function')
def browser():
    print('[FUNCTION] Открываем браузер на каждый автотест')


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        pass

    def test_user_can_create_course(self, settings, user, browser):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        pass
