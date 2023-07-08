from recipes.test.test_recipe_base import RecipeTestBase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewsTestCase(RecipeTestBase):

  #HOME
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



  #CATEGORY
  def test_recipe_category_views_function_is_correct(self):
    view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
    self.assertIs(view.func, views.category)

  def test_recipes_category_views_returns_404_if_no_recipes_found(self):
    response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
    self.assertEqual(response.status_code, 404)

  def test_recipes_category_template_loads_recipes(self):
    needed_title = 'this is a category page - It load category`s recipe'
    recipe = self.make_recipe(title=needed_title)
    response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.category.id}))
    content = response.content.decode('utf-8')

    # valores padrões do método make_recipe
    self.assertIn(needed_title, content)
    self.assertIn('description', content)
    self.assertIn('5 porções', content)
    self.assertIn('10 minutes', content)

  def test_recipes_category_template_dont_loads_recipes_not_publish(self):
    recipe = self.make_recipe(is_published=False)
    response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))

    self.assertEqual(response.status_code, 404)

  def test_recipes_category_views_loads_correct_template(self):
    recipe = self.make_recipe(is_published=True)
    response = self.client.get(reverse('recipes:category', kwargs={'category_id': recipe.category.id}))
    self.assertTemplateUsed(response, 'recipes/pages/category.html')


  #DETAILS RECIPE
  def test_recipe_detail_views_function_is_correct(self):
    view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
    self.assertIs(view.func, views.recipe)

  def test_recipes_detail_views_returns_404_if_no_recipes_found(self):
    response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
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