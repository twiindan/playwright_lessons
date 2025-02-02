from playwright.sync_api import Page

URL = 'https://jqueryui.com/droppable/'


def test_drag_and_drop_manually(page: Page):
    page.goto(URL)
    page.wait_for_timeout(1000)
    page.locator(".demo-frame").content_frame.locator("#draggable").hover()
    page.mouse.down()
    page.locator(".demo-frame").content_frame.locator("#droppable").hover()
    page.mouse.up()
    page.wait_for_timeout(2000)


def test_drag_and_drop(page: Page):
    page.goto(URL)
    page.wait_for_timeout(1000)
    page.locator(".demo-frame").content_frame.locator("#draggable").drag_to(page.locator(".demo-frame").content_frame.locator("#droppable"))
    page.wait_for_timeout(2000)
