from playwright.sync_api import Page, expect


def test_product_card(page: Page) -> None:

    page.goto('https://www.demoblaze.com/')
    page.locator(".card.h-100").filter(has_text="Samsung galaxy s6").click()
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="Add to cart").click()
    page.get_by_role("link", name="Cart", exact=True).click()

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text='Price').count() > 0:
            price_col_index = index
            break

    product_row = page.locator("tr").filter(has_text="Samsung galaxy s6")
    expect(product_row.locator("td").nth(price_col_index)).to_have_text("360")
