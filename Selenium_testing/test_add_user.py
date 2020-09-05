"""
    Test of adding user on demosite
"""

import unittest
from selenium import webdriver


class TestAddUser(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(options=options)

    def test_title(self):
        self.driver.get("http://thedemosite.co.uk/addauser.php")
        self.assertEqual(self.driver.title, 'Add a user - FREE PHP code and SQL')

    def test_adding_user_succeeded(self):
        self.driver.get("http://thedemosite.co.uk/addauser.php")
        username_elem = self.driver.find_element_by_name("username")
        password_elem = self.driver.find_element_by_name("password")
        username_elem.send_keys("user0987")
        password_elem.send_keys("pass123")
        elem = self.driver.find_element_by_name("FormsButton2")
        elem.click()
        elem = self.driver.find_element_by_tag_name("blockquote")
        #elem1= self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/blockquote/blockquote[2]/blockquote')
        self.assertIn('user0987', elem.text)
        self.assertIn('pass123', elem.text)

    def test_adding_user_failed(self):
        self.driver.get("http://thedemosite.co.uk/addauser.php")
        username_elem = self.driver.find_element_by_name("username")
        password_elem = self.driver.find_element_by_name("password")
        username_elem.send_keys("u")
        password_elem.send_keys("pass123")
        elem = self.driver.find_element_by_name("FormsButton2")
        elem.click()
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, 'Username too short.  The username must be at least 4 characters in length.')
        alert.accept()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
