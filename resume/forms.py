from django import forms
from resume.models import Document, Education, Experience, Referee

class DateInput(forms.DateInput):
    input_type = 'date'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['user', 'created', 'updated']
        widgets = {
            'from_date': DateInput(),
            'to_date': DateInput()
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ['user', 'created', 'updated']
        widgets = {
            'from_date': DateInput(),
            'to_date': DateInput()
        }

class RefereeForm(forms.ModelForm):
    class Meta:
        model = Referee
        exclude = ['user', 'created', 'updated']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['user', 'created', 'updated']
        widgets = {
            'file': forms.ClearableFileInput(
                attrs={
                    'multiple': True
                }
            ),
        }