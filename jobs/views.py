from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from jobs.models import Job, Application

class JobsListView(LoginRequiredMixin, ListView):
    queryset = Job.objects.filter(is_open=True)
    context_object_name = "jobs"
    template_name = "jobs/jobs.html"

class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    context_object_name = "job"
    template_name = "jobs/job-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        
        try:
            is_applied = Application.objects.get(applicant=self.request.user,parent_job=self.get_object())
        except Application.DoesNotExist:
            is_applied = None

        context["is_applied"] = is_applied

        return context

    def post(self, request, *args, **kwargs):
        parent_job = self.get_object()
        user = request.user
        try:
            Application.objects.get(applicant=user, parent_job=parent_job)
            messages.error(request, "You have already applied for this role")
            return HttpResponseRedirect(self.request.get_full_path())
        except Application.DoesNotExist:
            new_application = Application(
                applicant = user, parent_job=parent_job,
            )
            new_application.save()
            messages.success(request, "Application sent")
            return HttpResponseRedirect(self.request.get_full_path())


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    context_object_name = "applications"
    template_name = "jobs/application_list.html"