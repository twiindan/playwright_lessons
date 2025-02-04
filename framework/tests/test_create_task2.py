from playwright.sync_api import Page, expect

from framework.models.task import Task
from framework.pages.main_page import MainPage
from framework.pages.task_page import TaskPage


def test_create_task(login_with_auth: Page):

    page = login_with_auth
    main_page = MainPage(page)
    main_page.go_to_create_new_task()

    task_page = TaskPage(page)
    task_page.create_new_task(title='testing3', description='testing3', priority="3")
    expect(page.get_by_role("cell", name="testing1")).to_have_text("testing1")


def test_complete_task(login_with_auth: Page):

    title_task = 'completed3'
    page = login_with_auth
    main_page = MainPage(page)
    main_page.go_to_create_new_task()

    task_page = TaskPage(page)
    task_page.create_new_task(title=title_task, description=title_task, priority="3")
    expect(main_page.get_cell_locator_by_title(title_task)).to_have_text(title_task)

    main_page.complete_task(title_task)
    expect(main_page.get_cell_locator_by_title(title_task)).to_have_class("strike-through-td")


def test_complete_task_with_faker(login_with_auth: Page, random_task: Task):

    page = login_with_auth
    main_page = MainPage(page)
    main_page.go_to_create_new_task()

    task_page = TaskPage(page)
    task_page.create_new_task(title=random_task.title, description=random_task.description,
                              priority=random_task.priority)
    expect(main_page.get_cell_locator_by_title(random_task.title)).to_have_text(random_task.title)

    main_page.complete_task(random_task.title)
    expect(main_page.get_cell_locator_by_title(random_task.title)).to_have_class("strike-through-td")
