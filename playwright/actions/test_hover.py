from playwright.sync_api import Page


URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_hover(page: Page):
    page.goto(URL)
    page.locator('#mousehover').hover()
    page.wait_for_timeout(5000)





