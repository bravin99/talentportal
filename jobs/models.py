from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class JobsModelsBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Job(JobsModelsBase):
    title = models.CharField(max_length=155)
    positions = models.IntegerField(default=1)
    salary = models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True)
    description = models.TextField()
    requirements = models.TextField()
    apply_by = models.DateTimeField()


class Application(JobsModelsBase):
    STATUS_CHOICES = (
        ('ap', 'Applied'),
        ('si', 'Scheduled Interview'),
        ('hi', 'Hired'),
        ('dp', 'dropped')
    )
    applicant = models.ForeignKey(User, related_name="application", on_delete=models.CASCADE)
    parent_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ap")