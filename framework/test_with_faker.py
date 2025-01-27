from playwright.sync_api import Page, expect
from models.user import User


def test_register_basic(page: Page, random_user: User) -> None:
    page.goto("https://todotesting.azurewebsites.net/auth/")
    page.get_by_role("link", name="Register ?").click()
    page.locator("#email").click()
    page.locator("#email").fill(random_user.email)
    page.locator("#username").click()
    page.locator("#username").fill(random_user.username)
    page.locator("#firstname").click()
    page.locator("#firstname").fill(random_user.firstname)
    page.locator("#lastname").click()
    page.locator("#lastname").fill(random_user.lastname)
    page.locator("#password").click()
    page.locator("#password").fill(random_user.password)
    page.locator("input[name=\"password2\"]").click()
    page.locator("input[name=\"password2\"]").fill(random_user.password)
    page.locator("#register").click()
    page.locator("#username").click()
    page.locator("#username").fill(random_user.username)
    page.locator("#password").click()
    page.locator("#password").fill(random_user.password)
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Logout").click()
