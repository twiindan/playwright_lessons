from playwright.sync_api import Page, expect


URL = 'https://rahulshettyacademy.com/seleniumPractise/#/offers'


def test_tables(page: Page):

    page.goto(URL)
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text='Price').count() > 0:
            price_col_index = index
            break

    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(price_col_index)).to_have_text("37")
