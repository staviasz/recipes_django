from django.urls import resolve, reverse
from recipes import views
from recipes.test.test_recipe_base import RecipeTestBase

class RecipeViewHomeTest(RecipeTestBase):
  def test_recipe_home_views_function_is_correct(self):
    view = resolve(reverse('recipes:home'))
    self.assertIs(view.func, views.home)

  def test_recipes_home_views_returns_status_200_ok(self):
    response = self.client.get(reverse('recipes:home'))
    self.assertEqual(response.status_code, 200)

  def test_recipes_home_views_loads_correct_template(self):
    response = self.client.get(reverse('recipes:home'))
    self.assertTemplateUsed(response, 'recipes/pages/home.html')

  def test_recipes_home_template_shows_no_recipes_found_if_no_recipes(self):
    response = self.client.get(reverse('recipes:home'))
    self.assertIn('No recipes found here', response.content.decode('utf-8'))

  def test_recipes_home_template_loads_recipes(self):
    needed_title = 'the home page'
    self.make_recipe(title=needed_title)
    response = self.client.get(reverse('recipes:home'))
    content = response.content.decode('utf-8')

    # valores padrões do método make_recipe
    self.assertIn(needed_title, content)
    self.assertIn('description', content)
    self.assertIn('5 porções', content)
    self.assertIn('10 minutes', content)

  def test_recipes_home_template_dont_loads_recipes_not_publish(self):
    self.make_recipe(is_published=False)
    response = self.client.get(reverse('recipes:home'))

    self.assertIn('No recipes found here', response.content.decode('utf-8'))

