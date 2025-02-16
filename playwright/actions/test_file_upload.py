from playwright.sync_api import Page, expect


def test_file_upload(page: Page):
    page.goto('http://letcode.in/file')
    page.locator('.file-input')
    with page.expect_file_chooser() as fc_info:
        page.locator('.file-cta').click()
    file_chooser = fc_info.value
    file_chooser.set_files("README.md")
    expect(page.locator('p.label')).to_have_text('Selected File: README.md')
