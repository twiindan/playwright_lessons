from playwright.sync_api import Page, expect


def test_to_have_attribute(page: Page):

    page.goto('http://localhost:8000/v1.0/demo')
    expect(page.get_by_placeholder("Hide/Show Example")).to_have_attribute("type", "text")


def test_to_have_values(page: Page):

    page.goto('http://localhost:8000/v1.0/demo')
    locator = page.locator('#multiple-select-example')
    locator.select_option(['apple', 'orange', 'peach'])
    expect(locator).to_have_value('apple')
    expect(locator).to_have_values(['apple', 'orange', 'peach'])


