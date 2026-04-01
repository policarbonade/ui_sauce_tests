from pages.base_page import BasePage


class GooglePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("textarea[name='q']")

    def open(self):
        self.page.goto("https://www.saucedemo.com")

    def search(self, text):
        self.search_input.fill(text)
        self.search_input.press("Enter")
        self.page.locator("h3").first.wait_for()

    def get_title(self):
        return self.page.title()