from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError

from recipes.models import Recipe
from authors.validators import AuthorRecipeValidator
from utils.form_utils import add_attr

class AuthorRecipeForm(forms.ModelForm):
  def __init__(self,*args,**kwargs):
    super().__init__(*args, **kwargs)

    self._my_errors = defaultdict(list)

    add_attr(self.fields.get('preparation_steps'), 'class', 'span-2')

  class Meta:
    model = Recipe
    fields = (
      'title', 'description', 'preparation_time',
      'preparation_time_unit', 'servings', 'servings_unit',
      'preparation_steps', 'cover'
    )

    widgets = {
      'cover': forms.FileInput(
        attrs={
          'class': 'span-2'
        }
      ),
      'servings_unit': forms.Select(
        choices=(
          ('porções', 'Porções'),
          ('pedaços', 'Pedaços'),
          ('pessoas', 'Pessoas')
        )
      ),
      'preparation_time_unit': forms.Select(
        choices=(
          ('minutos', 'Minutos'),
          ('horas', 'Horas'),
        )
      ),
    }

  def clean(self, *args, **kwargs):
    super_clean = super().clean(*args, **kwargs)
    AuthorRecipeValidator(self.cleaned_data, ErrorClass=ValidationError)
    return super_clean


  #   cleaned_data = self.cleaned_data

  #   title = self.cleaned_data.get('title')
  #   description = cleaned_data.get('description')

  #   if title == description:
  #     self._my_errors['title'].append('Cannot be equal to description')
  #     self._my_errors['description'].append('Cannot be equal to title')

  #   if self._my_errors:
  #     raise ValidationError(self._my_errors)

  #   return super_clean

  # def clean_title(self):
  #   title = self.cleaned_data.get('title')

  #   if len(title) < 5:
  #     self._my_errors['title'].append('Must have at least 5 chars')

  #   return title

  # def clean_preparation_time(self):
  #   field_value = self.cleaned_data.get('preparation_time')
  #   if not is_positive_number(field_value):
  #     self._my_errors['preparation_time'].append('Must be a positive number')

  #   return field_value

  # def clean_servings(self):
  #   field_value = self.cleaned_data.get('servings')
  #   if not is_positive_number(field_value):
  #     self._my_errors['servings'].append('Must be a positive number')

  #   return field_value


