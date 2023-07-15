import pytest

from unittest.mock import patch
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from tests.base_functional_test import BaseFunctionalTest


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(BaseFunctionalTest):

  @patch('recipes.views.PER_PAGE', new=6)
  def test_recipe_home_page_without_recipes_error_messages(self):
    self.browser.get(self.live_server_url)
    body = self.browser.find_element(By.TAG_NAME, 'body')
    self.assertIn('No recipes found here', body.text)

  @patch('recipes.views.PER_PAGE', new=6)
  def test_recipe_search_input_can_find_correct_recipes(self):
    recipes = self.make_recipe_in_batch()
    self.browser.get(self.live_server_url)
    search_input = self.browser.find_element(
      By.XPATH,
      '//input[@placeholder="Search for a recipe"]'
    )
    title_needed = recipes[0].title
    search_input.send_keys(title_needed)
    search_input.send_keys(Keys.ENTER)

    self.assertIn(
      title_needed,
      self.browser.find_element(By.CLASS_NAME, 'main-content-list').text
    )

  @patch('recipes.views.PER_PAGE', new=2)
  def test_recipe_page_pagination(self):
    self.make_recipe_in_batch()
    self.browser.get(self.live_server_url)
    page2 = self.browser.find_element(
      By.XPATH,
      '//a[@aria-label="Go to page 2"]'
    )
    page2.click()
    self.assertEqual(
      len(self.browser.find_elements(
        By.CLASS_NAME, 'recipe'
      )),
      2
    )

