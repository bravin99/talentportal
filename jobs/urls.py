from django.urls import path

from jobs import views
urlpatterns = [
    path('listing/', views.JobsListView.as_view(), name="jobs"),
]