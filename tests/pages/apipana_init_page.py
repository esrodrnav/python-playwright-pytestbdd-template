from playwright.sync_api import Page, expect

class ApipanaInitPage:
    def __init__(self, page: Page, get_env_datas):
        self.page = page
        self.data = {}
        self.test_datas = get_env_datas
        self.mas_info_button = self.page.locator(f'//a[contains(@class, "elementor-button")]/span/span[text() = "{self.test_datas.get("language").get("es").get("mas_info_button")}"]')
        self.mas_info_modal = self.page.locator('//div[@class = "elementor-background-overlay"]')
    
     
    def click_mas_info_button(self):
        self.mas_info_button.scroll_into_view_if_needed()
        self.mas_info_button.click()

    def verify_mas_info_modal_displayed(self):
        expect(self.mas_info_modal, 'The más info modal does not display').to_be_visible()