from playwright.sync_api import expect, Page


def test_basic_duckduckgo_search(page: Page) -> None:
    # Given the DuckDuckGo home page is displayed
    page.goto('https://www.duckduckgo.com')

    # When the user searches for a phrase
    page.locator('#searchbox_input').fill('python')
    page.locator("button[type='submit']").click()
    # Then the search result query is the phrase
    expect(page.locator('#search_form_input')).to_have_value('python')

    # And the search result links pertain to the phrase
    result_locators = page.get_by_test_id("result-title-a").all()
    for locator in result_locators:
        assert "python" in locator.text_content().lower()

    # And the search result title contains the phrase
    expect(page).to_have_title('python at DuckDuckGo')

