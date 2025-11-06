from playwright.sync_api import Page, expect

class nosostrosPage:

    def __init__(self, page: Page, get_env_datas):
        self.page = page
        self.test_datas = get_env_datas
        self.page_title = self.page.locator(f"//h2[text() = {self.test_datas.get('language').get('es').get('page_title')}]")


    def verify_page_title(self):
        expect(self.page_title, "El título no está visible").to_be_visible()
        title_text_expected = "Quiénes Somos"
        current_page_title = self.page_title.text_content()
        assert current_page_title == title_text_expected, f"El título de la página es incorrecto. Se esperaba '{title_text_expected}', pero se obtuvo '{current_page_title}'"
