from playwright.sync_api import Page
from tests.pages.base_page import BasePage


class LoginPage:
    def __init__(self, page: Page, get_env_datas):
        self.page = page
        self.data = {}
        self.test_datas = get_env_datas
        self.username_input = self.page.locator('//input[@data-test = "username"]')
        self.password_input = self.page.locator('//input[@data-test = "password"]')
        self.login_button = self.page.locator('//input[@id = "login-button"]')
    
     
    def enter_credentials(self):
        self.username_input.fill(self.test_datas.get("valid_user").get('username'))
        self.password_input.fill(self.test_datas.get("valid_user").get('password'))

    def click_login_button(self):
        self.login_button.click()
        

