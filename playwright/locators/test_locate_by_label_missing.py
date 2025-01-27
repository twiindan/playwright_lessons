from playwright.sync_api import Page


def test_playwright_shortcut(page: Page):
    page.goto('http://localhost:8000/v1.0/demo')
    label_text = page.get_by_label('Windows')
    print(label_text.text_content())
