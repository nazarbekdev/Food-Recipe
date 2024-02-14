from rest_framework.serializers import ModelSerializer
from api.models.category import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
