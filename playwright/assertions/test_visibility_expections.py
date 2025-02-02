from playwright.sync_api import Page, expect


URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_is_visible(page: Page):

    page.goto(URL)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()


def test_is_not_visible(page: Page):

    page.goto(URL)
    page.wait_for_timeout(1000)
    page.locator('#hide-textbox').click()
    page.wait_for_timeout(1000)
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


def test_is_hidden(page: Page):

    page.goto(URL)
    page.wait_for_timeout(1000)
    page.locator('#hide-textbox').click()
    page.wait_for_timeout(1000)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


def test_is_editable(page: Page):

    page.goto(URL)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_editable()
