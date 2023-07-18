from django.urls import resolve, reverse
from recipes import views
from recipes.test.test_recipe_base import RecipeTestBase

class RecipeViewDetailTest(RecipeTestBase):
  def test_recipe_detail_views_function_is_correct(self):
    view = resolve(reverse('recipes:recipe', kwargs={'pk': 1}))
    self.assertIs(view.func.view_class, views.RecipeDetailViewRecipe)

  def test_recipes_detail_views_returns_404_if_no_recipes_found(self):
    response = self.client.get(reverse('recipes:recipe', kwargs={'pk': 1000}))
    self.assertEqual(response.status_code, 404)

  def test_recipes_detail_template_loads_recipes(self):
    needed_title = 'this is a detail page - It load one recipe'
    self.make_recipe(title=needed_title)
    response = self.client.get(reverse('recipes:recipe', args=(1,)))
    content = response.content.decode('utf-8')

    # valores padrões do método make_recipe
    self.assertIn(needed_title, content)
    self.assertIn('description', content)
    self.assertIn('5 porções', content)
    self.assertIn('10 minutes', content)


