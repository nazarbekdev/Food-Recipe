from django.urls import path
from accounts.views.authorization import RegisterGenericAPIView, PasswordResetEmailGenericAPIView, \
    SetNewPasswordGenericAPIView, LogoutGenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views.follow import FollowGenericAPIView, UnFollowAPIView, FollowingUserGenericAPIView, \
    FollowersUserGenericAPIView, DeleteFollowerAPIView
from accounts.views.personal_data import PersonalDataGenericAPIView
from accounts.views.profile import ProfileGenericAPIView
from accounts.views.user_info import UserInfoGenericAPIView

urlpatterns = [
    path('register', RegisterGenericAPIView.as_view(), name='register'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout', LogoutGenericAPIView.as_view(), name='logout'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset-email', PasswordResetEmailGenericAPIView.as_view(), name='reset-email'),
    path('password-reset-complete/<uidb64>/<token>/', SetNewPasswordGenericAPIView.as_view(), name='password-reset-complete'),
    path('follow', FollowGenericAPIView.as_view(), name='follow'),
    path('unfollow/<int:user_id>', UnFollowAPIView.as_view(), name='unfollow'),
    path('delete-follower/<int:user_id>', DeleteFollowerAPIView.as_view(), name='delete-follower'),
    path('following', FollowingUserGenericAPIView.as_view(), name='following'),
    path('followers', FollowersUserGenericAPIView.as_view(), name='followers'),
    path('personal-data', PersonalDataGenericAPIView.as_view(), name='personal-data'),
    path('user-info', UserInfoGenericAPIView.as_view(), name='user-info'),
    path('profile', ProfileGenericAPIView.as_view(), name='profile'),
]
