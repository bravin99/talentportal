from django.urls import path

from jobs import views
urlpatterns = [
    path('listing/', views.JobsListView.as_view(), name="jobs"),
    path('job/<slug:slug>/', views.JobDetailView.as_view(), name='job-detail'),
    path('myapplications/', views.ApplicationListView.as_view(), name="my-applications"),
]