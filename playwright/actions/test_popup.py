from playwright.sync_api import Page

URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_get_pop_up(page: Page):
    page.goto(URL)
    with page.expect_popup() as popup_info:
        page.get_by_test_id("OpenTab").click()
    popup = popup_info.value
    print(popup.url)



