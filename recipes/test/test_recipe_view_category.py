from django.urls import resolve, reverse
from recipes import views
from recipes.test.test_recipe_base import RecipeTestBase

class RecipeViewCategoryTest(RecipeTestBase):
  def test_recipe_category_views_function_is_correct(self):
    view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
    self.assertIs(view.func.view_class, views.RecipeListViewCategory)

  def test_recipes_category_views_returns_404_if_no_recipes_found(self):
    response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
    self.assertEqual(response.status_code, 404)

  def test_recipes_category_template_loads_recipes(self):
    needed_title = 'this is a category page - It load category`s recipe'
    recipe = self.make_recipe(title=needed_title)
    response = self.client.get(reverse('recipes:recipe', kwargs={'pk': recipe.category.id}))
    content = response.content.decode('utf-8')

    # valores padrões do método make_recipe
    self.assertIn(needed_title, content)
    self.assertIn('description', content)
    self.assertIn('5 porções', content)
    self.assertIn('10 minutes', content)

  def test_recipes_category_template_dont_loads_recipes_not_publish(self):
    recipe = self.make_recipe(is_published=False)
    response = self.client.get(reverse('recipes:recipe', kwargs={'pk': recipe.id}))

    self.assertEqual(response.status_code, 404)

  def test_recipes_category_views_loads_correct_template(self):
    recipe = self.make_recipe(is_published=True)
    response = self.client.get(reverse('recipes:category', kwargs={'category_id': recipe.category.id}))
    self.assertTemplateUsed(response, 'recipes/pages/category.html')


