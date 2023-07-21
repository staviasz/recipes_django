from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError
from utils.is_positive_number import is_positive_number


class AuthorRecipeValidator:
  def __init__(self,data, errors=None, ErrorClass=None):
    self.errors = defaultdict(list) if errors is None else errors
    self.ErrorClass = defaultdict(list) if ErrorClass is None else ErrorClass
    self.data = data
    self.clean()

  def clean(self, *args, **kwargs):
    self.clean_title()
    self.clean_servings()
    self.clean_preparation_time()
    cleaned_data = self.data
    title = self.data.get('title')
    description = cleaned_data.get('description')
    if title == description:
      self.errors['title'].append('Cannot be equal to description')
      self.errors['description'].append('Cannot be equal to title')
    if self.errors:
      raise ValidationError(self.errors)

  def clean_title(self):
    title = self.data.get('title', '')
    if len(title) < 5:
      self.errors['title'].append('Must have at least 5 chars')
    return title

  def clean_preparation_time(self):
    field_value = self.data.get('preparation_time')
    if not is_positive_number(field_value):
      self.errors['preparation_time'].append('Must be a positive number')
    return field_value

  def clean_servings(self):
    field_value = self.data.get('servings')
    if not is_positive_number(field_value):
      self.errors['servings'].append('Must be a positive number')
    return field_value


