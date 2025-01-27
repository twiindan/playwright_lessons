from playwright.sync_api import Page


class MainPage:

    def __init__(self, page: Page):
        self.page = page
        self.logout_locator = page.get_by_role("link", name="Logout")

    def get_logout_locator(self):
        return self.logout_locator
