import re

from playwright.sync_api import Page
URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_playwright_shortcut(page: Page):

    # Can find by a complete string or substring.

    page.goto(URL)
    title_text = page.get_by_text("Practice Page")
    print(title_text.text_content())
    title_text = page.get_by_text("Practice")
    print(title_text.text_content())
    title_text = page.get_by_text("Practice Page", exact=True)
    print(title_text.text_content())
    title_text = page.get_by_text(re.compile("practice page", re.IGNORECASE))
    print(title_text.text_content())


    # title_text = page.get_by_text("Practice", exact=True)
    # print(title_text.text_content())
