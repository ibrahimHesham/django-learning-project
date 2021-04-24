from django.urls import path

from .views import SignUpView
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api/login', obtain_auth_token),
    path('api/signup', views.apiSignup),
]