from playwright.sync_api import Page

URL = 'https://arnaumarch.com/'

'''
One method to find resources in DOM is using XPATH. The idea is use different techniques
and tips to obtain a unique element in the webpage using Xpath selectors.
'''

'''Syntax for XPATH
    / --> Look for the element immdiately inside the parent element
    // --> Loof for any child or nested-child element inside the parent element

    //tag[@attribute=value]

Example

//div[@id="main-content"]/section[1]/header/menu/a
     vs

//div[@id="main-content"]//menu/a

'''


def test_playwright_complete_xpath(page: Page):
    page.goto(URL)
    open_window_button = page.locator('//div[@id="main-content"]/section[1]/header/menu/a')
    print(open_window_button.is_visible())


def test_playwright_nested_xpath(page: Page):
    page.goto(URL)
    open_window_button = page.locator('//div[@id="main-content"]//menu/a')
    print(open_window_button.is_visible())

'''
Be careful:

//div[@id="main-content"]/section[2]/div/article[2]/header
//div[@id="main-content"]/section[2]//header
'''


def test_playwright_complete_xpath_one_result(page: Page):
    page.goto(URL)
    open_window_button = page.locator('//div[@id="main-content"]/section[2]/div/article[2]/header')
    print(open_window_button.is_visible())


def test_playwright_nested_xpath_more_than_one_result(page: Page):
    page.goto(URL)
    open_window_button = page.locator('//div[@id="main-content"]/section[2]//header')
    print(open_window_button.is_visible())
    # strict mode violation. Locators are strict.
    # This means that all operations on locators that imply some target DOM element will throw an exception
    # if more than one element matches


'''
Using Text of the element to build an effective XPATH

//tag[text()=<element_text>]

//div[@id="main-content"]/section[2]/div/article[2]/header  -> Text "About me"

//header[text()='About me']

Also can use hierarchy:

//div[@id="main-content"]//header[text()="About me"]
'''


def test_playwright_complete_xpath_by_text(page: Page):
    page.goto(URL)
    open_window_button = page.locator('//header[text()="About me"]')
    print(open_window_button.is_visible())


'''
Another utility to serch elements is using another attributes with the command "Contains"

//tag[contains(attribute, 'value')]

//div[@id="main-content"]//header[contains(text(), "About me")]
//div[@id="main-content"]//a[contains(@class, "button")]

Several conditions can be used to matching:

//div[@id="main-content"]//a[contains(@class, "button") and contains(@href, "https://twitter.com/rnowm/")]

'''


def test_playwright_xpath_contains_text(page: Page):
    page.goto(URL)
    open_window_button = page.locator('//div[@id="main-content"]//header[contains(text(), "About me")]')
    print(open_window_button.is_visible())


def test_playwright_xpath_contains_class_name_failing(page: Page): #fail
    page.goto(URL)
    open_window_button = page.locator('//div[@id="main-content"]//a[contains(@class, "button")]')
    print(open_window_button.is_visible())


def test_playwright_xpath_contains_combined(page: Page):
    page.goto(URL)
    open_window_button = page.locator('//div[@id="main-content"]//a[contains(@class, "button") and '
                                                'contains(@href, "https://twitter.com/rnowm/")]')
    print(open_window_button.is_visible())

'''
Similar to contains function, XPATH also provide the starts-with function.

//tag[starts-with(attribute, value)]

//div[@id="main-content"]//header[starts-with(text(), "About")]
//div[@id="main-content"]//a[starts-with(@class, "butt")]
'''


def test_playwright_xpath_start_with(page: Page):
    page.goto(URL)
    open_window_button = page.locator('//div[@id="main-content"]//h1[starts-with(text(), "Hi")]')
    print(open_window_button.is_visible())
