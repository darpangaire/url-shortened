from django.urls import path
from .views import UserRegistrationView,VerifyEmailView,UserLoginView

urlpatterns = [
  path("api-register/",UserRegistrationView.as_view(),name='apiRegister'),
  path("api/verify-email/<uidb64>/<token>/",VerifyEmailView.as_view(),name='verify-email'),
  
  path('api-login/',UserLoginView.as_view(),name='api-login'),
  
]




