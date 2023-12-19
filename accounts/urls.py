from django.urls import path, include
from rest_framework import routers
from . import views
from .views import UserBankViewSet, UserViewSet, UserDateViewSet

app_name = 'accounts'

urlpatterns = [
    path('google/login', views.google_login, name='google_login'),
    path('google/callback/', views.google_callback, name='google_callback'),  
    path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
    path('bank', UserBankViewSet.as_view(), name='bank'),
    path('mypage', UserViewSet.as_view(), name='mypage'),
    path('date', UserDateViewSet.as_view(), name='date'),
]