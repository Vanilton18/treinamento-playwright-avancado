# test_search.py
from pages.search import SearchPage
from playwright.sync_api import Page, expect
import pytest


# No teste
class TestBing:
    def test_search_bing(self, page: Page):
        search_page = SearchPage(page)
        search_page.navigate()
        search_page.search("search query")
        page.pause()
        page.wait_for_selector('text=resultados')
        expect(page.get_by_text("resultados").first).to_be_visible()

    def test_search_bing_2(self, page: Page):
        search_page = SearchPage(page)
        search_page.navigate()
        search_page.search("search query2")
        page.wait_for_selector('text=resultados')
        expect(page.get_by_text("resultados333").first).to_be_visible()

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_skip_example(self):
        assert 1 == 2
