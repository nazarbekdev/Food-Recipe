from rest_framework.serializers import ModelSerializer
from api.models.comment import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user_id',)

    def create(self, validated_data):
        user_id = self.context['request'].user
        return Comment.objects.create(user_id=user_id, **validated_data)
