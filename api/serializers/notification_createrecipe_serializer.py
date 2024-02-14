from rest_framework.serializers import ModelSerializer
from api.models.notification_created_recipe import NotificationCreateRecipe


class NotificationCreateRecipeSerializer(ModelSerializer):
    class Meta:
        model = NotificationCreateRecipe
        fields = '__all__'
