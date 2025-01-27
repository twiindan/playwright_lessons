from playwright.sync_api import Page, expect


def test_to_have_title(page: Page):

    page.goto('http://localhost:8000/v1.0/demo')
    expect(page).to_have_title('Python for testers')


def test_to_have_url(page: Page):

    url = 'http://localhost:8000/v1.0/demo'
    page.goto(url)
    expect(page).to_have_url(url)
