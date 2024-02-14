from rest_framework.serializers import ModelSerializer
from accounts.models.user_follow import UserFollow
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowSerializer(ModelSerializer):
    class Meta:
        model = UserFollow
        fields = '__all__'
        read_only_fields = ('from_user',)

    def create(self, validated_data):
        from_user = self.context['request'].user
        return UserFollow.objects.create(from_user=from_user, **validated_data)


class FollowingFollowersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'avatar')
