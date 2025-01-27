from playwright.sync_api import Page

from exercises.framework.models.user import User


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username_locator = page.get_by_label("Username")
        self.password_locator = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Sign In")
        self.alert_locator = page.locator(".alert.alert-info")

    def login(self, user: User):
        self.username_locator.fill(user.username)
        self.password_locator.fill(user.password)
        self.login_button.click()

    def get_success_alert_locator(self):

        return self.alert_locator
