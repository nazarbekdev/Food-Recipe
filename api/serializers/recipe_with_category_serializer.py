from rest_framework.serializers import ModelSerializer
from api.models.dish import Dish


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'image', 'cocking_time')
