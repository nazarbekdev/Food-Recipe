from rest_framework.serializers import ModelSerializer
from api.models.recipe_rate import RecipeRate


class RecipeRateSerializer(ModelSerializer):
    class Meta:
        model = RecipeRate
        fields = '__all__'
        read_only_fields = ('user_id',)

    def create(self, validated_data):
        user_id = self.context['request'].user
        return RecipeRate.objects.create(user_id=user_id, **validated_data)
