from django.urls import path
from social_auth.views.facebook_auth import FacebookLogin, RedirectToFacebookApiView, callback_facebook
from social_auth.views.google_auth import GoogleLogin, RedirectToGoogleAPIView, callback_google

urlpatterns = [
    path('google', GoogleLogin.as_view(), name='google_login'),
    path('google-login', RedirectToGoogleAPIView.as_view(), name='google_login2'),
    path('google/callback', callback_google, name='google_callback'),
    path('facebook', FacebookLogin.as_view(), name='facebook'),
    path('facebook-login', RedirectToFacebookApiView.as_view(), name='facebook-login'),
    path('facebook/callback', callback_facebook, name='facebook_callback')
]
