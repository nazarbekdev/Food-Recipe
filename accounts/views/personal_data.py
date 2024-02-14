from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from accounts.serializers.personal_data_serializer import PersonalDataSerializer

User = get_user_model()


class PersonalDataGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PersonalDataSerializer

    def patch(self, request):
        user = User.objects.get(pk=request.user.id)
        serializer = self.get_serializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

