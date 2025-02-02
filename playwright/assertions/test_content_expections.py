import re

from playwright.sync_api import Page, expect


URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_is_empty(page: Page):

    page.goto(URL)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_empty()


def test_have_text(page: Page):
    input_data = 'Open Window'
    page.goto(URL)
    expect(page.locator("#openwindow")).to_have_text(input_data)


def test_have_text_regular_expression(page: Page):

    page.goto(URL)
    expect(page.locator("#openwindow")).to_have_text(re.compile(r"Open .*"))
