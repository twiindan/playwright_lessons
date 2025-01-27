from playwright.sync_api import Page

from exercises.framework.models.user import User


class RegisterPage:

    URL = 'https://microblog-hwepgvgtb6hchvcf.westeurope-01.azurewebsites.net/auth/register'

    def __init__(self, page: Page):
        self.page = page
        self.email_locator = page.locator("#email")
        self.username_locator = page.locator("#username")
        self.password_locator = page.locator("#password")
        self.verify_password_locator = page.locator("#password2")
        self.register_button_locator = page.locator("#submit")

    def load(self):
        self.page.goto(self.URL)

    def register_user(self, user: User):
        self.email_locator.fill(user.email)
        self.username_locator.fill(user.username)
        self.password_locator.fill(user.password)
        self.verify_password_locator.fill(user.password)
        self.register_button_locator.click()
