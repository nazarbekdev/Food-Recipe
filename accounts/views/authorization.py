from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from accounts.serializers.authorization_serializer import RegisterSerializer, PasswordResetEmailSerializer, SetNewPasswordSerializer, LogoutSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str, smart_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from accounts.user_utils.send_email_user import send_mail


User = get_user_model()


class RegisterGenericAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        confirm_password = request.data['confirm_password']
        if password != confirm_password:
            return Response({'message': 'Passwords do not match'}, status=400)

        if User.objects.filter(email=email).exists():
            return Response({'message': 'Email already exists'}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True})


class PasswordResetEmailGenericAPIView(GenericAPIView):
    serializer_class = PasswordResetEmailSerializer

    def post(self, request):
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = request.get_host()
            relativeLink = reverse(
                'password-reset-complete',
                kwargs={
                    'uidb64': uidb64,
                    'token': token,
                }
            )
            absurl = 'http://' + current_site + relativeLink
            email_body = 'Hello, \n Use link bellow to reset your password \n' + absurl
            data = {
                'email_subject': 'Reset your password',
                'email_body': email_body,
                'to_email': user.email,
            }
            send_mail.delay(data)
            return Response({'success': 'We have sent you a link to reset your password'}, status=200)
        return Response(status=404)


class SetNewPasswordGenericAPIView(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request, uidb64, token):
        try:
            password = request.data['password']
            confirm_password = request.data['confirm_password']

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            if password != confirm_password:
                return Response({'error': 'Passwords are not same'}, status=401)

            user.set_password(password)
            user.save()
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return Response({'succes': True, 'message': 'Password reset success'}, status=200)


class LogoutGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=204)
