from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.main_page import MainPage
from framework.models.user import User


from playwright.sync_api import Page, expect


def test_register_basic(page: Page, random_user: User) -> None:

    # Load login page
    login_page = LoginPage(page=page)
    login_page.load()

    # Navigate to register
    login_page.go_to_register()

    # register user
    register_page = RegisterPage(page=page)
    register_page.register_user(random_user)

    # login user
    login_page.login(random_user.username, random_user.password)

    #assert the main page
    main_page = MainPage(page=page)
    expect(main_page.logout_button_locator).to_be_visible()
    return MainPage