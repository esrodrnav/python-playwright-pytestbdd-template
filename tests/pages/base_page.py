from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page, get_env_datas):
        self.test_datas = get_env_datas
        self.page = page
        self.base_url = get_env_datas.get("base_url")

    def navigate_to_base_url(self):
        self.page.goto(self.base_url)