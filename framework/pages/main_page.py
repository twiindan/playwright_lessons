from playwright.sync_api import Page


class MainPage:

    URL = 'https://todotesting.azurewebsites.net/'

    def __init__(self, page: Page):
        self.page = page
        self.logout_button_locator = page.get_by_role("link", name="Logout")
        self.add_new_task_button_locator = page.get_by_role("link", name="Add a new Todo!")

    def load(self):
        self.page.goto(self.URL)

    def go_to_create_new_task(self):
        self.add_new_task_button_locator.click()

    def complete_task(self, title):
        self.page.get_by_role("row").filter(has_text=title).locator(".btn-success").click()

    def get_cell_locator_by_title(self, title):
        return self.page.get_by_role("cell", name=title)
