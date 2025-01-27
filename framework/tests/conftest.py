import pytest
from faker import Faker
from playwright.sync_api import expect, Browser, Page

from framework.models.user import User
from framework.models.task import Task
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage


@pytest.fixture(scope="session", autouse=True)
def random_user() -> User:
    return User(
        email=Faker().email(),
        username=Faker().name(),
        firstname=Faker().name(),
        lastname=Faker().name(),
        password=Faker().password(),
    )


@pytest.fixture(scope="session", autouse=True)
def random_task() -> Task:
    return Task(
        title=Faker().text(max_nb_chars=20),
        description=Faker().sentence(),
        priority=str(Faker().random_int(min=1, max=5))
    )


# @pytest.fixture(scope="session", autouse=True)
# def register_and_login(browser: Browser, random_user: User) -> None:
#
#     page = browser.new_context().new_page()
#
#     # Load login page
#     login_page = LoginPage(page=page)
#     login_page.load()
#
#     # Navigate to register
#     login_page.go_to_register()
#
#     # register user
#     register_page = RegisterPage(page=page)
#     register_page.register_user(random_user)
#
#     # login user
#     login_page.login(random_user.username, random_user.password)
#
#     #assert the main page
#     main_page = MainPage(page=page)
#     expect(main_page.logout_button_locator).to_be_visible()
#     return page


# @pytest.fixture(scope="session", autouse=True)
# def login(browser: Browser, random_user: User) -> None:
#
#     page = browser.new_context().new_page()
#
#     # Load login page
#     login_page = LoginPage(page=page)
#     login_page.load()
#
#     # login user
#     login_page.login('testing', 'testing')
#
#     #assert the main page
#     main_page = MainPage(page=page)
#     expect(main_page.logout_button_locator).to_be_visible()
#     page.context.storage_state(path="auth.json")
#
#     return page


@pytest.fixture(scope="session", autouse=True)
def login_with_auth(browser: Browser, random_user: User) -> Page:

    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    main_page = MainPage(page)
    main_page.load()

    return page

