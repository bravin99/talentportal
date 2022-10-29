from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from jobs.models import Job, Application

class JobsListView(LoginRequiredMixin, ListView):
    queryset = Job.objects.filter(is_open=True)
    context_object_name = "jobs"
    template_name = "jobs/jobs.html"

class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    context_object_name = "job"
    template_name = "jobs/job-detail.html"
    