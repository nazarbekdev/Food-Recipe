from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers.new_recipe_serializer import NewRecipeGetSerializer
from api.models.dish import Dish
from api.models.recipe_rate import RecipeRate
from django.contrib.auth import get_user_model

User = get_user_model()


class AllRecipe(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewRecipeGetSerializer

    def get(self, request):
        recipes = Dish.objects.all()
        serializers = self.get_serializer(recipes, many=True)
        serializer_data = serializers.data

        for data in serializer_data:
            dish_id = data['id']
            user_id = data['user_id']
            recipe_rate = RecipeRate.objects.filter(dish_id=dish_id).first()
            user_name = User.objects.filter(id=user_id).first()
            data['user_name'] = user_name.first_name + ' ' + user_name.last_name
            if recipe_rate:
                data['rate'] = recipe_rate.rate
            else:
                data['rate'] = 0

        return Response(serializer_data)
