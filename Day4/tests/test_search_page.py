from pages.home_page import HomePage
from pages.search_page import SearchPage
import unittest
import HtmlTestRunner

from test_template import TestTemplate

class TestSearchPage(TestTemplate):

    def test_result_found(self):
        home_page = HomePage(self._driver)
        home_page.set_search_query("Design pattern")
        home_page.search()
        result = SearchPage(self._driver)
        assert result.heading_text() == "Design pattern"

        
if __name__ == "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = 'reports'))