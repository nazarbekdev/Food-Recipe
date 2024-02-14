from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models.recipe_rate import RecipeRate
from api.serializers.recipe_rate_serializer import RecipeRateSerializer


class RateToRecipeGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeRateSerializer

    def post(self, request):
        if RecipeRate.objects.filter(user_id=request.user.id, dish_id=request.data['dish_id']).exists():
            return Response(status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
