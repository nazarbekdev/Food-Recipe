from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView

from accounts.models.user_follow import UserFollow
from accounts.serializers.follow_serializer import FollowSerializer, FollowingFollowersSerializer

User = get_user_model()


class FollowGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowSerializer

    def post(self, request):
        if request.user.id == request.data['to_user']:
            return Response(status=400)

        if UserFollow.objects.filter(from_user=request.user.id, to_user=request.data['to_user']).exists():
            return Response(status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class UnFollowAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, user_id):
        follow_user = UserFollow.objects.get(from_user=request.user.id, to_user=user_id)
        follow_user.delete()
        return Response(status=204)


class DeleteFollowerAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, user_id):
        follower = UserFollow.objects.get(from_user=user_id, to_user=request.user.id)
        follower.delete()
        return Response(status=204)


class FollowingUserGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowingFollowersSerializer

    def get(self, request):
        following_users = UserFollow.objects.filter(from_user=request.user.id)
        data_list = []
        for following_user in following_users:
            user = User.objects.get(pk=following_user.to_user.pk)
            serializer = self.get_serializer(user)
            data_list.append(serializer.data)
        return Response(data_list, status=200)


class FollowersUserGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowingFollowersSerializer

    def get(self, request):
        following_users = UserFollow.objects.filter(to_user=request.user.id)
        data_list = []
        for follow_user in following_users:
            user = User.objects.get(pk=follow_user.from_user.pk)
            serializer = self.get_serializer(user)
            data_list.append(serializer.data)
        return Response(data_list, status=200)

