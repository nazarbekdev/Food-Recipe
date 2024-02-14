from rest_framework.generics import ListAPIView
from rest_framework import filters
from api.models.dish import Dish
from api.serializers.search_serializer import SearchRecipeSerializer


class SearchRecipeListAPIView(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = SearchRecipeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
