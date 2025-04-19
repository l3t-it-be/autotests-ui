from enum import Enum


class AppRoute(str, Enum):
    LOGIN = './#/auth/login'
    REGISTRATION = './#/auth/registration'
    DASHBOARD = './#/dashboard'
    CREATE_COURSE = './#/courses/create'
    COURSES_LIST = './#/courses'
