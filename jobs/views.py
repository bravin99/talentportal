from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from jobs.models import Job, Application

class Jobs(LoginRequiredMixin, ListView):
    queryset = Job.objects.filter(is_open=True)