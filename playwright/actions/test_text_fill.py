from playwright.sync_api import Page


URL = 'https://gmail.com'

def test_gmail(page: Page):
    page.goto('https://gmail.com')
    page.locator('#identifierId').fill('twiindan@gmail.com')
    page.locator('#identifierNext').click()
    page.wait_for_timeout(5000)
