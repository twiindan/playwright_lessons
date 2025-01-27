from playwright.sync_api import Page, expect

from exercises.framework.models.user import User
from page.login_page import LoginPage
from page.main_page import MainPage
from page.register_page import RegisterPage


def test_register_user(page: Page, random_user: User):

    register_page = RegisterPage(page)
    register_page.load()

    register_page.register_user(user=random_user)
    login_page = LoginPage(page)
    expect(login_page.get_success_alert_locator()).to_have_text('Congratulations, you are now a registered user!')

    login_page.login(user=random_user)
    main_page = MainPage(page)
    expect(main_page.get_logout_locator()).to_be_visible()
