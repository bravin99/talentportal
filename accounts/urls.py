from django.urls import path
from accounts import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>[0-9A-Za-z_\-]/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  views.activate, name='activate'),
    path('profile/', views.profile, name='profile'),
]