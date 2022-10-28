from django.urls import path
from resume import views


urlpatterns = [
    path('', views.MyDetailsView.as_view(), name='mydetails'),
]