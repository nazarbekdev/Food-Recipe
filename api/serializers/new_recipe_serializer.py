from rest_framework.serializers import ModelSerializer
from api.models.dish import Dish


class NewRecipeGetSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'cocking_time', 'user_id', 'image')
