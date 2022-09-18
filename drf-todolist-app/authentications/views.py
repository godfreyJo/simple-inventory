from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .utils import Util
from django.contrib.sites.shortcuts import get_current_sites

# Create your views here.

class RegisterView(generics.GenericAPIView):

    serializer_class=RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user=User.objects.get(email=user_data['email'])

        token=RefreshToken.for_user(user)
        current_sites=get_current_sites(request)

        data={'domain':current_sites.domain}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)
    
class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass

