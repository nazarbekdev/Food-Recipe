from rest_framework.serializers import ModelSerializer
from api.models.notification_saved_recipe import NotificationSaveRecipe


class NotificationSaveRecipeSerializer(ModelSerializer):
    class Meta:
        model = NotificationSaveRecipe
        fields = '__all__'
