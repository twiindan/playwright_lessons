from playwright.sync_api import Page


class TaskPage:

    def __init__(self, page: Page):

        self.page = page
        self.task_title_locator = page.locator("input[name=\"title\"]")
        self.task_description = page.locator("textarea[name=\"description\"]")
        self.task_priority = page.get_by_role("combobox")
        self.add_new_task_button = page.get_by_role("button", name="Add new todo")

    def create_new_task(self, title: str, description: str, priority: str):

        self.task_title_locator.fill(title)
        self.task_description.fill(description)
        self.task_priority.select_option(priority)
        self.add_new_task_button.click()
