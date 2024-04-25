from rest_framework.serializers import ModelSerializer

from api.models.dish import Dish


class SearchRecipeSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'user_id', 'image')
