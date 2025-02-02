from playwright.sync_api import Page


URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_browser_resize(page: Page):
    page.set_viewport_size({"width": 640, "height": 480})
    page.goto(URL)


def test_browser_navigation(page: Page):
    page.goto('https://google.com')
    page.goto(URL)

    page.go_back()
    page.go_forward()
    page.reload()
    page.close()
