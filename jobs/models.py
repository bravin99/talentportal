from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from django.utils.crypto import get_random_string

User = get_user_model()

class JobsModelsBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Job(JobsModelsBase):
    title = models.CharField(max_length=155)
    slug = models.SlugField(unique=True, blank=True, help_text="Auto generated")
    job_type = models.CharField(max_length=35, null=True, blank=True, help_text="e.g internship, entry level, ...")
    contract_type = models.CharField(max_length=35, help_text="e.g temporary, full time, ...")
    positions = models.IntegerField(default=1)
    salary = models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True)
    description = models.TextField()
    requirements = models.TextField()
    apply_by = models.DateTimeField()
    is_open = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            rand_string = get_random_string(length=6)
            self.slug = slugify(self.title + '-' + rand_string)
        return super(Job, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'slug': self.slug})

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

    class Meta:
        ordering = ['-created']