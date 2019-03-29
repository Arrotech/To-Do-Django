import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class TestLearnApp(unittest.TestCase):
	"""Test the app."""

	def setUp(self):
		"""Setup the app."""
		# Open Firefox
		self.browser = webdriver.Firefox()

	def tearDown(self):
		"""Tear down the app."""
		# Qiut Firefox
		self.browser.quit()

	def test_home_page(self):
		"""Test that django is correctly installed."""
		# Access the computer local port 8000
		self.browser.get('http://localhost:8000')
		# Assert the django message
		self.assertIn('Learn', self.browser.title)
		header = self.browser.find_element_by_tag_name('h1')
		self.assertIn('Learn', header.text)

		# Find element input by user by id.
		inputbox = self.browser.find_element_by_id('new_item_id')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Input Item')
		inputbox.send_keys('Learn django')

		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('list_table_id')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue('1: Learn django', [row.text for row in rows])

		# Finish the test after success
		self.fail('finish this test')

if __name__ == '__main__':
	unittest.main()


