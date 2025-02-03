import playwright.sync_api
from playwright.sync_api import Page

URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_playwright_shortcut(page: Page):
    page.goto(URL)
    open_window_button = page.get_by_test_id("OpenTab")
    print(open_window_button.is_visible())


def test_set_test_id(page: Page):
    from playwright.sync_api import sync_playwright, Playwright
    playwright.sync_api.Selectors.set_test_id_attribute('data-testingid')
    page.goto(URL)
    placeholder = page.get_by_test_id("placeholder")
    print(placeholder.is_visible())
