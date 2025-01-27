from playwright.sync_api import Page, expect


def test_register_user(page: Page):

    # Load Main Page
    page.goto('https://microblog-hwepgvgtb6hchvcf.westeurope-01.azurewebsites.net/')

    # Go to Register page
    page.get_by_role("link", name="Click to Register!").click()

    # Fill all data to create new user and register it.
    page.locator('#username').fill('testing4')
    page.locator("#email").fill("testing4@testing.com")
    page.locator("#password").fill("testing4@testing.com")
    page.locator("#password2").fill("testing4@testing.com")
    page.locator("#submit").click()

    #validate user is created
    expect(page.locator(".alert.alert-info")).to_have_text('Congratulations, you are now a registered user!')


    #login
    page.get_by_label("Username").fill("testing")
    page.get_by_label("Password").fill("testing")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
