# pages/search.py

class SearchPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://bing.com")
        print(self.page.title())

    def search(self, text):
        self.page.wait_for_timeout(2000)
        search_term_input = self.page.locator("[name='q']")
        search_term_input.click()
        search_term_input.fill(text)
        search_term_input.press("Enter")
