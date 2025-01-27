from playwright.sync_api import Page

from framework.models.user import User


class RegisterPage:

    URL = 'https://todotesting.azurewebsites.net/auth/register'

    def __init__(self, page: Page):
        self.page = page
        self.email_locator = page.locator("#email")
        self.first_name_locator = page.locator("#firstname")
        self.last_name_locator = page.locator("#lastname")
        self.username_locator = page.locator("#username")
        self.password_locator = page.locator("#password")
        self.verify_password_locator = page.locator("input[name=\"password2\"]")
        self.register_button_locator = page.locator("#register")

    def load(self):
        self.page.goto(self.URL)

    def register_user(self, user: User):
        self.email_locator.fill(user.email)
        self.username_locator.fill(user.username)
        self.first_name_locator.fill(user.firstname)
        self.last_name_locator.fill(user.lastname)
        self.password_locator.fill(user.password)
        self.verify_password_locator.fill(user.password)
        self.register_button_locator.click()
