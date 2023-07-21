from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from recipes.models import Category, Recipe
from recipes.serializers import CategorySerializer, RecipeSerializer

# class B(IsAuthenticated):
#   def has_permission(self, request, view):
#     authorization_header = request.META.get('HTTP_AUTHORIZATION')
#     print('TOKEN ===', authorization_header)
#     print('USER ===', request.user)
#     print('IS_AUTHENTICATED ===', request.user.is_authenticated)
#     print('RESULT ===', request.user and request.user.is_authenticated)
#     return bool(request.user and request.user.is_authenticated)

class RecipeAPIv2Pagination(PageNumberPagination):
  page_size = 2


class RecipeAPIv2ViewSet(ModelViewSet):
  queryset = Recipe.objects.get_published()
  serializer_class = RecipeSerializer
  pagination_class = RecipeAPIv2Pagination


class RecipeApiCategory(RetrieveUpdateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer



