class BasePage:

    def __init__(self, page):
        self.page = page
        self.search_input = page.locator("textarea[name='q']")

    def open(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)