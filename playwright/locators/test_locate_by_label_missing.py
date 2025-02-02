from playwright.sync_api import Page

URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_playwright_shortcut(page: Page):
    page.goto(URL)
    label_text = page.get_by_label('Windows')
    print(label_text.text_content())
