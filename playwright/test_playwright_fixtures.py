from time import sleep
from playwright.sync_api import Page


def test_playwright_basic(playwright):
    browser = playwright.chromium.launch(headless=False)  # Chromium is the base for Chrome and Edge
    context = browser.new_context()  # Every context is a new window without shared context
    page = context.new_page()
    page.goto('https://google.es')


def test_playwright_multiple_contexts(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://google.es')
    sleep(2)
    page = context.new_page()
    page.goto('https://google.es')
    sleep(2)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://google.es')
    sleep(3)


# Chromium Headless Mode, 1 single context.
# If you want to change the headless mode you can do it in the execution options --headed
def test_playwright_shortcut(page: Page):
    page.goto('https://google.es')
