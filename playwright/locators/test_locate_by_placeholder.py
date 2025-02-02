from playwright.sync_api import Page

URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_playwright_shortcut(page: Page):
    page.goto(URL)
    placeholder_text = page.get_by_placeholder('Enter Your Name')
    print(placeholder_text.is_visible())
