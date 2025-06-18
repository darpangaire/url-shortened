from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializers,LoginUserSerializers
from rest_framework.response import Response
from rest_framework import status
from.utils import send_verification_email

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
# Create your views here.

User = get_user_model()

def get_tokens_for_user(user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
  def post(self,request,format=None):
    serializers = UserRegistrationSerializers(data = request.data)
    if serializers.is_valid():
      user = serializers.save()
      send_verification_email(user,request)
      
      return Response({
        "message":"User Registration Successfully",
        "user":serializers.data
      },status=status.HTTP_201_CREATED)
      
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
  
  
# Create a View to Handle Verification Link
class VerifyEmailView(APIView):
  def get(self,request,uidb64,token):
    try:
      uid = urlsafe_base64_decode(uidb64).decode()
      user = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
      user = None
      
    if user and default_token_generator.check_token(user,token):
      user.is_active = True
      user.save()
      return Response({"message":"Email Verified Successfully"},status=status.HTTP_200_OK)
      
    return Response({"error":"Invalid or expired token"},status=status.HTTP_400_BAD_REQUEST)
  
       
class UserLoginView(APIView):
  def post(self,request,format=None):
    serializers = LoginUserSerializers(data = request.data, context={'request': request})
    if serializers.is_valid():
      user = serializers.validated_data['user']
      token = get_tokens_for_user(user)
      return Response({"msg":"Login Successfull","token":token},status=status.HTTP_200_OK)
      
    else:
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
      
 
    