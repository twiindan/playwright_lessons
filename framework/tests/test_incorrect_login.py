import json

from framework.pages.login_page import LoginPage
from framework.models.user import User
from playwright.sync_api import Page, expect
import pytest


with open("../data/credentials.json") as credential_file:
    test_data = json.load(credential_file)
    user_credentials_list = test_data['user_credentials']


def test_incorrect_login_basic(page: Page, random_user: User) -> None:

    login_page = LoginPage(page=page)
    login_page.load()
    login_page.login(username='incorrect_user', password='bad_pwd')
    expect(login_page.get_alert_locator()).to_be_visible()


@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_incorrect_login_parametrized(page: Page, random_user: User, user_credentials) -> None:

    login_page = LoginPage(page=page)
    login_page.load()
    login_page.login(username=user_credentials['username'], password=user_credentials['password'])
    expect(login_page.get_alert_locator()).to_be_visible()
