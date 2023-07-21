from rest_framework import serializers

from recipes.models import Category, Recipe
from authors.validators import AuthorRecipeValidator


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['name']

class RecipeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recipe
    fields = ['id', 'title', 'description', 'author',
              'category', 'category_links','preparation_time',
              'preparation_time_unit', 'servings', 'servings_unit',
              'preparation_steps', 'cover'
            ]
  category = serializers.StringRelatedField()
  category_links = serializers.HyperlinkedRelatedField(
    source='category',
    view_name='recipes:recipe_api_v2_category',
    read_only=True
  )

  def validate(self, attrs):
    if self.instance is not None and attrs.get('servings') is None:
      attrs['servings'] = self.instance.servings
    if self.instance is not None and attrs.get('preparation_time') is None:
      attrs['preparation_time'] = self.instance.preparation_time
    super_validate = super().validate(attrs)
    AuthorRecipeValidator(data=attrs, ErrorClass=serializers.ValidationError)
    return super_validate



