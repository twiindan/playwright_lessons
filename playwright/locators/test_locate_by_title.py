from playwright.sync_api import Page

URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_playwright_shortcut(page: Page):
    page.goto(URL)
    open_window_button = page.get_by_title("Open Window")
    print(open_window_button.is_visible())

