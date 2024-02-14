from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.models.user_follow import UserFollow
from api.models.dish import Dish
from api.models.notification_saved_recipe import NotificationSaveRecipe
from api.models.saved_dish import SavedDish
from api.serializers.saved_recipe import SavedRecipeSerializer, SavedRecipeDetailSerializer, SaveDishPostSerializer
from django.contrib.auth import get_user_model
from api.api_utils.recipe_rate import recipe_rate

User = get_user_model()


class SaveRecipePostView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SaveDishPostSerializer

    def post(self, request):
        save_recipe = self.get_serializer(data=request.data)
        save_recipe.is_valid(raise_exception=True)
        save_recipe.validated_data['user_id'] = request.user
        save_recipe.save()
        userfollows = UserFollow.objects.filter(from_user=request.user)
        for userfollow in userfollows:
            print(userfollow.to_user_id)
        notification = NotificationSaveRecipe.create_saved_recipe_notification(user=request.user)
        return Response({'success': True, 'message': 'Notification sent successfully'})


class SavedRecipeGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SavedRecipeSerializer

    def get(self, request):
        saved_recipe = SavedDish.objects.filter(user_id=request.user.id)
        saved_recipe_list = []
        for sr in saved_recipe:
            dish = Dish.objects.get(id=sr.dish_id.id)
            serializer = self.get_serializer(dish)
            serialized_data = serializer.data
            serialized_data['rate'] = recipe_rate(dish_id=serialized_data['id'])
            serialized_data['author_name'] = User.objects.get(id=request.user.id).first_name
            saved_recipe_list.append(serialized_data)
        return Response(saved_recipe_list)


class SavedRecipeDetailGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SavedRecipeDetailSerializer

    def get(self, request, dish_id):
        try:
            saved_recipe = SavedDish.objects.get(user_id=request.user.id, dish_id=dish_id)
        except SavedDish.DoesNotExist:
            return Response(status=400)

        saved_recipe_detail = Dish.objects.get(id=saved_recipe.dish_id.id)
        serializer = self.get_serializer(saved_recipe_detail)
        serialized_data = serializer.data
        try:
            serialized_data['author_avatar'] = User.objects.get(id=request.user.id).avatar.url
        except:
            serialized_data['author_avatar'] = None
        serialized_data['author_name'] = User.objects.get(id=request.user.id).first_name
        serialized_data['author_location'] = User.objects.get(id=request.user.id).location
        serialized_data['rate'] = recipe_rate(dish_id)
        return Response(serialized_data)


class UnSaveRecipeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, dish_id):
        try:
            saved_recipe = SavedDish.objects.get(user_id=request.user, dish_id=dish_id)
            saved_recipe.delete()
            return Response(status=204)
        except Exception as e:
            return Response({'message': str(e)}, status=400)


