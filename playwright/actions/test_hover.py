from playwright.sync_api import Page


def test_hover(page: Page):
    page.goto('http://localhost:8000/v1.0/demo')
    page.locator('#mousehover').hover()
    page.wait_for_timeout(5000)





