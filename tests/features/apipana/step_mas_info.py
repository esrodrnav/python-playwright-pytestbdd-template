import pytest
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page, expect
from tests.pages.apipana_init_page import ApipanaInitPage



scenarios("apipana_mas_info.feature")

@pytest.fixture
def apipana_init_page(page: Page, get_env_datas):
    return ApipanaInitPage(page, get_env_datas)


@when('clicks on "Más Info" button')
def click_mas_info_button(apipana_init_page):
    apipana_init_page.click_mas_info_button()

