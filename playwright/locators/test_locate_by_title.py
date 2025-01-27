from playwright.sync_api import Page


def test_playwright_shortcut(page: Page):
    page.goto('http://localhost:8000/v1.0/demo')
    open_window_button = page.get_by_title("Open Window")
    print(open_window_button.is_visible())

