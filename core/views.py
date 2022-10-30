from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from jobs.models import Application

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get(self, *args, **kwargs):
        user = self.request.user
        recent_applications = Application.objects.filter(applicant=user).order_by('-created')[:2]
        return self.render_to_response({
            'recent_applications': recent_applications
        })