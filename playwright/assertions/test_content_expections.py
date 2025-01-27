import re

from playwright.sync_api import Page, expect


def test_is_empty(page: Page):

    page.goto('http://localhost:8000/v1.0/demo')
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_empty()


def test_have_text(page: Page):
    input_data = 'Open Window'
    page.goto('http://localhost:8000/v1.0/demo')
    expect(page.locator("#openwindow")).to_have_text(input_data)


def test_have_text_regular_expression(page: Page):

    page.goto('http://localhost:8000/v1.0/demo')
    expect(page.locator("#openwindow")).to_have_text(re.compile(r"Open .*"))
