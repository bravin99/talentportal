from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ResumeBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Education(ResumeBaseModel):
    user = models.ForeignKey(User, related_name="education")
    from_date = models.DateField(verbose_name="From")
    to_date = models.DateField(verbose_name="To")
    institution_name = models.CharField(max_length=100)
    course = models.CharField(max_length=155)
    enrolled = models.BooleanField(help_text="Are you still attending for classes ?")
    grade = models.CharField(max_length=35)
    your_achievements = models.TextField()

