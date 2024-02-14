from rest_framework.serializers import ModelSerializer

from api.models.dish import Dish


class CreateDishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
        read_only_fields = ('user_id',)

    def create(self, validated_data):
        user_id = self.context['request'].user
        return Dish.objects.create(user_id=user_id, **validated_data)


class MyRecipeSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'image', 'cocking_time')


class MyRecipeDetailSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
