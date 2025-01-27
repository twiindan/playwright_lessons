import re
from playwright.sync_api import Page, expect


def test_register_basic(page: Page) -> None:
    page.goto("https://todotesting.azurewebsites.net/auth/")
    page.get_by_role("link", name="Register ?").click()
    page.locator("#email").click()
    page.locator("#email").fill("testing@testing.com")
    page.locator("#username").click()
    page.locator("#username").fill("testing")
    page.locator("#firstname").click()
    page.locator("#firstname").fill("toni")
    page.locator("#lastname").click()
    page.locator("#lastname").fill("robres")
    page.locator("#password").click()
    page.locator("#password").fill("testing")
    page.locator("input[name=\"password2\"]").click()
    page.locator("input[name=\"password2\"]").fill("testing")
    page.locator("#register").click()
    page.locator("#username").click()
    page.locator("#username").fill("testing")
    page.locator("#password").click()
    page.locator("#password").fill("testing")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Logout").click()
