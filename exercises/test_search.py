from playwright.sync_api import expect, Page


def test_basic_duckduckgo_search(page: Page) -> None:
    # Go to the DuckDuckGo page

    # Search "Python"

    # In the results check all the pages has the Python Word

    # Check the Window title is 'python at DuckDuckGo'

    # And the search result title contains the phrase
    pass
