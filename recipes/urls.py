from django.urls import path

from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewBase.as_view(), name="home"),
    path('recipes/search/', views.RecipeListViewSearch.as_view(), name="search"),
    path('recipes/category/<int:category_id>/',
         views.RecipeListViewCategory.as_view(), name="category"),
    path('recipes/<int:pk>/', views.RecipeDetailViewRecipe.as_view(), name="recipe"),

    # Api
    path('recipes/api/v1/', views.RecipeListViewHomeApi.as_view(), name="recipe_api"),
    path('recipes/api/v1/<int:pk>/',
         views.RecipeDetailViewRecipeApi.as_view(), name="recipe_api_detail"),
    path('recipes/api/v2/',
         views.recipe_api_list, name='recipe_api_v2')
]
