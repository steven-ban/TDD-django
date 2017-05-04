# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Edge()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text =self.browser.find_element_by_name('h1').text
        self.assertIn("To-Do", header_text)

        # input To-Do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # input "buy vegetable" in form
        inputbox.send_keys('buy vegetable')

        # Enter, refresed automatically and show "buy vegetable"
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: buy vegetable' for row in rows),
            "New to-do item did not appear in table"
        )

        # another form for input item
        # input "buy books"

        # refreshed automatically and show two items

        # generate URL for this operation
        # description for this page

        # go to URL, show two items

        self.fail('Finish the test!')



if __name__ == '__main__':
    unittest.main()