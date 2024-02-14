from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models.notification_saved_recipe import NotificationSaveRecipe
from api.serializers.notification_savedrecipe_serializer import NotificationSaveRecipeSerializer


class NotificationSaveGet(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSaveRecipeSerializer

    def get(self, request):
        notification = NotificationSaveRecipe.objects.filter(user=request.user.id)
        serializer = self.get_serializer(notification, many=True)
        data = serializer.data
        return Response(data)
