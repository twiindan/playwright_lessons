from playwright.sync_api import Page, expect


URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_to_have_title(page: Page):

    page.goto(URL)
    expect(page).to_have_title('Python for testers')


def test_to_have_url(page: Page):

    url = URL
    page.goto(url)
    expect(page).to_have_url(url)
