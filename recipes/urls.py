from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from recipes import views

app_name = 'recipes'
api_router = SimpleRouter()
api_router.register('recipes/api/v2', views.RecipeAPIv2ViewSet,)
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
    path('recipes/api/v2/category/<int:pk>/',
         views.RecipeApiCategory.as_view(), name='recipe_api_v2_category'),

    #JWT
    path('recipes/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('recipes/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recipes/api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]

urlpatterns += api_router.urls
