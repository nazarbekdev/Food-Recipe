import os
import requests
from allauth.socialaccount.models import SocialApp
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.views import get_user_model
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

User = get_user_model()


class RedirectToGoogleAPIView(APIView):

    def get(self, request):
        google_redirect_uri = os.getenv('GOOGLE_REDIRECT_URL')
        print('Google Redirect url------', google_redirect_uri)
        try:
            google_client_id = SocialApp.objects.get(provider='google').client_id
            print('Google CI ----- ', google_client_id)
        except SocialApp.DoesNotExist:
            return Response({'success': False, 'message': 'SocialApp does not exist'}, status=404)
        url = f'https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={google_redirect_uri}&prompt=consent&response_type=code&client_id={google_client_id}&scope=openid email profile&access_type=offline'
        return redirect(url)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'https://646b-178-218-201-17.ngrok-free.app/social-auth/google/callback'
    client_class = OAuth2Client


@api_view(["GET"])
def callback_google(request):
    """Callback"""
    code = request.GET.get("code")
    res = requests.post('https://646b-178-218-201-17.ngrok-free.app/social-auth/google', data={"code": code}, timeout=30)
    return Response(res.json())
