from django.urls import path
from core import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard"),
]