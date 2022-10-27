from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, View

class Dashboard(TemplateView):
    template_name = "core/dashboard.html"