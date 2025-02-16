from playwright.sync_api import Page


class MainPage:

    def __init__(self, page: Page):
        self.page = page
        self.logout_locator = page.get_by_role("link", name="Logout")
        self.post_textbox_locator = page.locator("#post")
        self.submit_button = page.locator("#submit")
        self.profile_locator = page.get_by_role("link", name="Profile")

    def get_logout_locator(self):
        return self.logout_locator

    def create_new_post(self, post_text):
        self.post_textbox_locator.fill(post_text)
        self.submit_button.click()

    def get_post_by_text(self, text):
        return self.page.locator("td").filter(has_text=text)

    def go_to_profile_page(self):
        self.profile_locator.click()

    def logout(self):
        self.logout_locator.click()
