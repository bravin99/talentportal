from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ResumeBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Education(ResumeBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education")
    from_date = models.DateField(verbose_name="From")
    to_date = models.DateField(verbose_name="To")
    institution_name = models.CharField(max_length=100)
    course = models.CharField(max_length=155)
    enrolled = models.BooleanField(help_text="Are you still attending for classes ?")
    grade = models.CharField(max_length=35)
    your_achievements = models.TextField()

class Experience(ResumeBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="experience")
    from_date = models.DateField(verbose_name="From")
    to_date = models.DateField(verbose_name="To")
    organization_name = models.CharField(max_length=100)
    position = models.CharField(max_length=40, help_text="Job title")
    salary = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Salary (Ksh)")
    description = models.TextField(verbose_name="Brief description of your roles")
    why_left = models.TextField(verbose_name="Reasons for leaving")
