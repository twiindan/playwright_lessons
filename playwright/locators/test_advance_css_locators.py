from playwright.sync_api import Page

URL = 'https://forumhtml.azurewebsites.net/v1.0/demo'
'''
One method to find resources in DOM is using CSS Selectors. The idea is use different techniques
and tips to obtain a unique element in the webpage using CSS selectors.
'''

'''Syntax for CSS Selectors
There are several possibilities to define a CSS Selector.
    - tag[attribute='value']
    - #Id
    - .Class
'''

'''
Example using Id's

input[id=displayed-text]
#displayed-text
input#displayed-text

'''


def test_playwright_css_by_id(page: Page):
    page.goto(URL)
    open_window_button = page.locator('input[id=displayed-text]')
    print(open_window_button.is_visible())

    open_window_button = page.locator('#displayed-text')
    print(open_window_button.is_visible())

    open_window_button = page.locator('input#displayed-text')
    print(open_window_button.is_visible())


'''
Example using Classes

input[class=displayed-class]
.displayed-class
.input.displayed-class

'''


def test_playwright_css_by_class(page: Page):
    page.goto(URL)
    open_window_button = page.locator('.displayed-class')
    print(open_window_button.is_visible())

    open_window_button = page.locator('input.displayed-class')
    print(open_window_button.is_visible())

    open_window_button = page.locator('.inputs.displayed-class')
    print(open_window_button.is_visible())

    open_window_button = page.locator('.btn-style.class1.class2')
    print(open_window_button.is_visible())


'''
Is Possible is wildcards inside the CSS Selectors using the following syntax:

tag[attribute<special-character>=value]

The special characters used as wildcards are the following:

    - Represents the starting text --> ^
    - Represents the ending text --> $
    - Represents the text contained --> *
'''


'''
Examples using wildcards

input[class='inputs'] --> 1 matching element
input[class^='inputs'] --> 2 matching element
input[class$='inputs'] --> 1 matching element
input[class*='inputs'] --> 2 matching element

'''


def test_playwright_css_wildcards(page: Page):
    page.goto(URL)
    open_window_button = page.locator("input[class='inputs']")
    print(open_window_button.is_visible())

    open_window_button = page.locator("input[class^='inputs']").all()
    print(len(open_window_button))

    open_window_button = page.locator("input[class$='inputs']")
    print(open_window_button.is_visible())

    open_window_button = page.locator("input[class*='inputs']").all()
    print(len(open_window_button))


'''
Is possible also find the elements finding his children nodes using the character ">".

fieldset>table
fieldset>#product
fieldset>button
fieldset>input#name
'''


def test_playwright_css_childrens(page: Page):
    page.goto(URL)
    open_window_button = page.locator("fieldset>table")
    print(open_window_button.is_visible())

    open_window_button = page.locator("fieldset>#product")
    print(open_window_button.is_visible())

    open_window_button = page.locator("fieldset>button")
    print(open_window_button.is_visible())

    open_window_button = page.locator("fieldset>input#name")
    print(open_window_button.is_visible())
