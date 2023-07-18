import os
from typing import Any
from django.db import models

from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView, DetailView

from recipes.models import Recipe
from utils.make_pagination import make_pagination

PER_PAGE = int(os.environ.get('PER_PAGE', 3))

class RecipeListViewBase(ListView):
  model = Recipe
  paginate_by = None
  context_object_name = 'recipes'
  ordering = ['-id']
  template_name = 'recipes/pages/home.html'

  def get_queryset(self, *args, **kwargs):
    qs = super().get_queryset(*args, **kwargs)
    qs = qs.filter(is_published=True)
    return qs

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    page_obj, pagination_range = make_pagination(
      self.request,
      context.get('recipes'),
      PER_PAGE
      )
    context.update({
      'recipes': page_obj,
      'pagination_range': pagination_range,
    })
    return context


class RecipeListViewCategory(RecipeListViewBase):
  template_name = 'recipes/pages/category.html'

  def get_queryset(self, *args, **kwargs):
    qs = super().get_queryset(*args, **kwargs)
    qs = qs.filter(
      category__id=self.kwargs.get('category_id')
    )
    if not qs:
      raise Http404()
    return qs

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context.update({
      'page_title': f'{context.get("recipes")[0].category.name} - Category | ',
    })
    return context


class RecipeListViewSearch(RecipeListViewBase):
  template_name = 'recipes/pages/search.html'
  def get_queryset(self, *args, **kwargs):
    search_term = self.request.GET.get('q', '').strip()
    if not search_term:
      raise Http404()
    qs = super().get_queryset(*args, **kwargs)
    qs = qs.filter(
      Q(
        Q(title__icontains=search_term) |
        Q(description__icontains=search_term),
      ),
      is_published=True
    )
    return qs

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    search_term = self.request.GET.get('q', '').strip()
    context.update({
      'page_title': f'Search for "{search_term}"',
      'search_term': search_term,
      'additional_url_query': f'&q={search_term}',
    })
    return context


class RecipeDetailViewRecipe(DetailView):
  model = Recipe
  context_object_name = 'recipe'
  template_name = 'recipes/pages/recipe-view.html'

  def get_queryset(self):
    qs = super().get_queryset()
    qs = qs.filter(is_published=True)
    return qs

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
    'is_detail_page': True,
    })
    return context

