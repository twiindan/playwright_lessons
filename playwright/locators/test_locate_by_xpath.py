from playwright.sync_api import Page

URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_playwright_css_basics(page: Page):
    page.goto(URL)
    open_window_button = page.locator("#displayed-text")
    print(open_window_button.is_visible())


def test_playwright_xpath_basics(page: Page):
    page.goto(URL)
    open_window_button = page.locator("//input[@id='name']")
    print(open_window_button.is_visible())
