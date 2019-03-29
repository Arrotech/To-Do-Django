from django.test import TestCase

class TestHomePage(TestCase):
	"""Test home page."""

	def test_home_template(self):
		"""Test addition of two numbers."""
		# Access homepage
		response = self.client.get('/')
		"""
		This is the content actual testing which is not necessary.
		# self.assertIn('<title>Learn</title>', response.content.decode())
		# self.assertTrue(response.content.decode().startswith('<html>'))
		# self.assertTrue(response.content.decode().endswith('</html>'))

		# Asserts that actually index template was used.
		"""

		# Refactoring the test.
		self.assertTemplateUsed(response, 'index.html')

	def test_add_new_item(self):
		"""Post requests"""
		response = self.client.post('/', {'Input': 'learn django'})
		self.assertIn('learn django', response.content.decode())


# Create your tests here.
