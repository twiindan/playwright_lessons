from playwright.sync_api import Page

URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'


def handle_dialog(dialog):
    print(dialog.message)
    dialog.accept()


def test_alert_dialog_with_lambda(page: Page):
    page.goto(URL)
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator('#alertbtn').click()


def test_alert_dialog(page: Page):
    page.goto(URL)
    page.on("dialog", handle_dialog)
    page.locator('#alertbtn').click()


def test_confirm_dialog_confirm(page: Page):
    page.goto(URL)
    page.on("dialog", handle_dialog)
    page.locator('#confirmbtn').click()


def test_confirm_dialog_dismiss(page: Page):
    page.goto(URL)
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.locator('#confirmbtn').click()

