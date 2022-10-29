from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from resume.forms import (DocumentForm, EducationForm, ExperienceForm,
                          RefereeForm)
from resume.models import Document, Education, Experience, Referee


class MyDetailsView(LoginRequiredMixin, TemplateView):
    template_name = "resume/mydetails.html"

    def get(self, request, *args, **kwargs):
        c_user = request.user
        education_form = EducationForm()
        experience_form = ExperienceForm()
        referee_form = RefereeForm()
        document_form = DocumentForm()
        return self.render_to_response({
            'c_user': c_user, 'education_form': education_form, 
            'experience_form':experience_form, 'referee_form': referee_form, 
            'document_form': document_form
        })

    def post(self, request, *args, **kwargs):
        education_form = EducationForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        referee_form = RefereeForm(request.POST)
        document_form = DocumentForm(request.POST)

        user = request.user

        if education_form.is_bound and education_form.is_valid():
            education_form.instance.user = user
            education_form.save()
            return HttpResponseRedirect(self.request.get_full_path())
        elif experience_form.is_bound and experience_form.is_valid():
            experience_form.instance.user = user
            experience_form.save()
            return HttpResponseRedirect(self.request.get_full_path())
        elif referee_form.is_bound and referee_form.is_valid():
            referee_form.instance.user = user 
            referee_form.save()
            return HttpResponseRedirect(self.request.get_full_path())
        elif document_form.is_bound and document_form.is_valid():
            document_form.instance.user = user
            document_form.save()
            return HttpResponseRedirect(self.request.get_full_path())

        return self.render_to_response({
            'education_form': education_form, 
            'experience_form':experience_form,
            'referee_form': referee_form, 
            'document_form': document_form
        })