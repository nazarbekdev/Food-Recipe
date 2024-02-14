from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.api_utils.recipe_rate import recipe_rate
from api.models.dish import Dish
from api.serializers.recipe_with_category_serializer import RecipeSerializer


class RecipeDataList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Dish.objects.all()

    def get(self, request, pk):
        recipe_data = Dish.objects.filter(category_id=pk)
        serializer = self.get_serializer(recipe_data, many=True)
        for recipe in serializer.data:
            recipe['rate'] = recipe_rate(recipe['id'])
        return Response(serializer.data)
