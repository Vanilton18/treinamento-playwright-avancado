# test_search.py
from pages.search import SearchPage
from playwright.sync_api import BrowserContext, expect


# No teste

def test_search_bing(context: BrowserContext):
    page = context.new_page()
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("search query")
    expect(page.get_by_text("resultados").first).to_be_visible()
