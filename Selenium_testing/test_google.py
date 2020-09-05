"""
    Basic selenium test google.com
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class TestBasics(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(options=options)

    def test_title(self):
        self.driver.get("https://www.google.pl")
        self.assertEqual(self.driver.title, 'Google')

    def test_element_visible(self):
        self.driver.get("https://www.google.pl")
        try:
            self.driver.find_element_by_name("q")
        except NoSuchElementException:
            self.fail("Element not found!")

    def test_wikipedia_link(self):
        self.driver.get("https://www.google.pl")
        elem = self.driver.find_element_by_name("q")
        # print(elem.text)
        elem.clear()
        elem.send_keys("Python")
        elem.send_keys(Keys.RETURN)
        self.assertIn('pl.wikipedia.org', self.driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
