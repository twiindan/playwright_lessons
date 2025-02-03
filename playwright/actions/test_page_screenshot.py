from playwright.sync_api import Page


URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_browser_navigation(page: Page):
    page.goto('https://google.com')
    page.goto(URL)
    page.screenshot(path="screenshot1.png", full_page=True)
    page.go_back()
    page.screenshot(path="screenshot2.png", full_page=True)
    page.go_forward()
    page.reload()
    page.close()
