from playwright.sync_api import Page

URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_playwright_fill_text(page: Page):
    page.goto(URL)
    placeholder_text = page.get_by_placeholder('Enter Your Name')
    placeholder_text.fill('Toni Robres')
    page.wait_for_timeout(5000)


def test_gmail(page: Page):
    page.goto('https://gmail.com')
    page.locator('#identifierId').fill('twiindan@gmail.com')
    page.wait_for_timeout(5000)

# There are more actions with click like double click, right button or click + keys.
# More information in https://playwright.dev/python/docs/input#mouse-click
