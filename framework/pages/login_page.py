from playwright.sync_api import Page


class LoginPage:

    URL = 'https://todotesting.azurewebsites.net/'

    def __init__(self, page: Page):
        self.page = page
        self.username_locator = page.locator("#username")
        self.password_locator = page.locator("#password")
        self.login_button_locator = page.locator("#login_button")
        self.register_link_locator = page.locator("#register_button")

    def load(self):
        self.page.goto(self.URL)

    def go_to_register(self):
        self.register_link_locator.click()

    def login(self, username: str, password: str):
        self.username_locator.fill(username)
        self.password_locator.fill(password)
        self.login_button_locator.click()
