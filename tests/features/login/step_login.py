from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page, expect


scenarios("login.feature")

@when("the user enters valid credentials")
def enter_valid_credentials(page):
    page.goto("https://playwright.dev/")

@then("the login is successful")
def verify_successful_login():
    pass