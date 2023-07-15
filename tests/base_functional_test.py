from recipes.test.test_recipe_base import RecipeMixin
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By




class BaseFunctionalTest(StaticLiveServerTestCase, RecipeMixin):
  def setUp(self):
    self.browser = make_chrome_browser('--headless')
    # self.browser = make_chrome_browser()
    return super().setUp()

  def tearDown(self):
    self.browser.quit()
    return super().tearDown()

  def get_by_input_name(self, web_element, value):
    return web_element.find_element(
      By.XPATH,
      f'//input[@name="{value}"]'
    )

