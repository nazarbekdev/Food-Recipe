from rest_framework.serializers import ModelSerializer
from django.contrib.auth.views import get_user_model

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar', 'bio', 'location')

