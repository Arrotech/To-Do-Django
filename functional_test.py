from selenium import webdriver

# Open firefox
browser = webdriver.Firefox()

# Access this port on my computer
browser.get('http://localhost:8000')

# Assert the test if django is installed
assert 'Django' in browser.title
