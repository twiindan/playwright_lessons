from playwright.sync_api import Page, expect


URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def test_radio_buttons(page: Page):
    page.goto(URL)
    page.locator('#windowsradio').check()
    expect(page.locator('#windowsradio')).to_be_checked()
    page.wait_for_timeout(1000)
    page.locator('#appleradio').check()
    expect(page.locator('#appleradio')).to_be_checked()
    page.wait_for_timeout(1000)
    page.locator('#linuxradio').check()
    expect(page.locator('#linuxradio')).to_be_checked()
    page.wait_for_timeout(1000)


def test_checkbox(page: Page):
    page.goto(URL)
    page.locator('#windowscheck').check()
    expect(page.locator('#windowscheck')).to_be_checked()
    page.wait_for_timeout(1000)
    page.locator('#linuxcheck').check()
    expect(page.locator('#linuxcheck')).to_be_checked()
    page.wait_for_timeout(1000)
    page.locator('#applecheck').check()
    expect(page.locator('#applecheck')).to_be_checked()
    page.wait_for_timeout(1000)
    page.locator('#applecheck').uncheck()
    expect(page.locator('#applecheck')).not_to_be_checked()

