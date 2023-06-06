from django.urls import path
from .views import signup

from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"

urlpatterns = [
    path('api/login', obtain_auth_token, name='api-login'),
    path('api/signup', signup, name='signup')
]
