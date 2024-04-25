# from rest_framework.generics import ListAPIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from api.models.notification_created_recipe import NotificationCreateRecipe
# from api.serializers.notification_createrecipe_serializer import NotificationCreateRecipeSerializer
#
#
# class NotificationCreateGet(ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = NotificationCreateRecipeSerializer
#
#     def get(self, request):
#         notification = NotificationCreateRecipe.objects.filter(to_user=request.user.id)
#         serializer = self.get_serializer(notification, many=True)
#         data = serializer.data
#         return Response(data)
