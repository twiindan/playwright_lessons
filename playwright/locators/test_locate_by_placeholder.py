from playwright.sync_api import Page


def test_playwright_shortcut(page: Page):
    page.goto('http://localhost:8000/v1.0/demo')
    placeholder_text = page.get_by_placeholder('Enter Your Name')
    print(placeholder_text.is_visible())
