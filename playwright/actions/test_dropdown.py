from playwright.sync_api import Page

URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_select_dropdown(page: Page):
    page.goto(URL)
    page.locator('#multiple-select-example').select_option(value='apple')
    page.wait_for_timeout(5000)


def test_select_multiple_dropdown(page: Page):
    page.goto(URL)
    page.locator('#multiple-select-example').select_option(['apple', 'orange', 'peach'])
    page.wait_for_timeout(5000)



