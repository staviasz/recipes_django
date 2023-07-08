from django.core.exceptions import ValidationError
from parameterized import parameterized

from recipes.test.test_recipe_base import RecipeTestBase, Recipe, Category


class RecipeModelTest(RecipeTestBase):
  def setUp(self) -> None:
    self.recipe = self.make_recipe()
    return super().setUp()

  @parameterized.expand([
      ('title', 65),
      ('description', 165),
      ('preparation_time_unit', 65),
      ('servings_unit', 65)
    ])
  def test_recipe_fields_max_length(self, field, max_length):
    setattr(self.recipe, field, 'A' * (max_length + 1))
    with self.assertRaises(ValidationError):
      self.recipe.full_clean()

  def test_preparation_steps_is_html_and_is_published_has_value_default_false(self):
    recipe = Recipe.objects.create(
      title = 'title' ,
      description = 'description' ,
      slug = 'slug-slug',
      preparation_time = 10 ,
      preparation_time_unit = 'minutes' ,
      servings = 5 ,
      servings_unit = 'porções' ,
      preparation_steps = 'preparation steps' ,
      category = self.make_category(name='the test category') ,
      author = self.make_author(username='the test author') ,
    )

    recipe.full_clean()
    recipe.save()
    self.assertFalse(recipe.preparation_steps_is_html)
    self.assertFalse(recipe.is_published)

  def test_recipe_string_representation(self):
    self.recipe.title = 'Testing Representation'
    self.recipe.full_clean()
    self.recipe.save()
    self.assertEqual(str(self.recipe), 'Testing Representation')


class CategoryModelTest(RecipeTestBase):
  def setUp(self):
    self.category = self.make_category(
      name='Category Testing'
    )
    return super().setUp()

  def test_category_string_representation(self):
    self.assertEqual(
      str(self.category),
      self.category.name
    )

  def test_category_name_max_length_is_65_chars(self):
    self.category.name = 'A' * 66
    with self.assertRaises(ValidationError):
      self.category.full_clean()

