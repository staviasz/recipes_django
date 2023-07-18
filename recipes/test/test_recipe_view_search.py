from django.urls import resolve, reverse
from recipes import views
from recipes.test.test_recipe_base import RecipeTestBase

class RecipeViewSearchTest(RecipeTestBase):
  def test_recipe_search_views_function_is_correct(self):
    view = resolve(reverse('recipes:search'))
    self.assertIs(view.func.view_class, views.RecipeListViewSearch)

  def test_recipes_search_views_loads_correct_template(self):
    response = self.client.get(reverse('recipes:search') + '?q=test')
    self.assertTemplateUsed(response, 'recipes/pages/search.html')

  def test_recipes_search_raise_404_if_no_search_term(self):
    response = self.client.get(reverse('recipes:search'))
    self.assertEqual(response.status_code, 404)

  def test_recipe_search_term_is_on_page_title_and_escaped(self):
    response = self.client.get(reverse('recipes:search') + '?q=test')
    self.assertIn(
      'Search for &quot;test&quot;',
      response.content.decode('utf-8')
    )

  def test_recipe_search_can_find_recipes_by_title(self):
    title1 = 'This is recipe one'
    title2 = 'This is recipe two'

    recipe1 = self.make_recipe(
      slug='one', title=title1, author_data={'username': 'one'}
    )
    recipe2 = self.make_recipe(
      slug='two', title=title2, author_data={'username': 'two'}
    )

    url = reverse('recipes:search')
    response1 = self.client.get(f'{url}?q={title1}')
    response2 = self.client.get(f'{url}?q={title2}')
    response_both = self.client.get(f'{url}?q=this')

    self.assertIn(recipe1, response1.context['recipes'])
    self.assertNotIn(recipe2, response1.context['recipes'])

    self.assertIn(recipe2, response2.context['recipes'])
    self.assertNotIn(recipe1, response2.context['recipes'])

    self.assertIn(recipe1, response_both.context['recipes'])
    self.assertIn(recipe2, response_both.context['recipes'])

  def test_recipe_search_can_find_recipes_by_description(self):
    description1 = 'This is recipe one'
    description2 = 'This is recipe two'

    recipe1 = self.make_recipe(
      slug='one', title=description1, author_data={'username': 'one'}
    )
    recipe2 = self.make_recipe(
      slug='two', title=description2, author_data={'username': 'two'}
    )

    url = reverse('recipes:search')
    response1 = self.client.get(f'{url}?q={description1}')
    response2 = self.client.get(f'{url}?q={description2}')
    response_both = self.client.get(f'{url}?q=this')

    self.assertIn(recipe1, response1.context['recipes'])
    self.assertNotIn(recipe2, response1.context['recipes'])

    self.assertIn(recipe2, response2.context['recipes'])
    self.assertNotIn(recipe1, response2.context['recipes'])

    self.assertIn(recipe1, response_both.context['recipes'])
    self.assertIn(recipe2, response_both.context['recipes'])
