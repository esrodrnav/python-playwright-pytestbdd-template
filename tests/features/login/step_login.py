import pytest
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page, expect
from tests.pages.login_page import LoginPage


scenarios("login.feature")

@pytest.fixture
def login_page(page: Page, get_env_datas):
    return LoginPage(page, get_env_datas)


@when("the user enters valid credentials")
def enter_valid_credentials(login_page):
    login_page.enter_credentials()
   

@then("the login is successful")
def verify_successful_login(login_page):
    pass