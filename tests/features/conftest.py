from pytest_bdd import given, when, then, scenario
from tests.pages.base_page import BasePage


@given("the user is on the login page")
def navigate_to_login_page(page, get_env_datas):
    base_page = BasePage(page, get_env_datas)
    base_page.navigate_to_base_url()
    