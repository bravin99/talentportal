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
    enrolled = models.BooleanField(default=False, help_text="Are you still attending for classes ?")
    grade = models.CharField(max_length=35)
    your_achievements = models.TextField()

    class Meta:
        ordering = ['-to_date']

class Experience(ResumeBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="experience")
    from_date = models.DateField(verbose_name="From")
    to_date = models.DateField(verbose_name="To")
    organization_name = models.CharField(max_length=100)
    position = models.CharField(max_length=40, help_text="Job title")
    salary = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Salary (Ksh)")
    description = models.TextField(verbose_name="Brief description of your roles")
    in_role = models.BooleanField(default=False, verbose_name="Are you still working here ?")
    why_left = models.TextField(verbose_name="Reasons for leaving")

    class Meta:
        ordering = ['-to_date']

class Referee(ResumeBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="referees")
    referee_name = models.CharField(max_length=155)
    organization_name = models.CharField(max_length=155)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    call = models.BooleanField(default=True, verbose_name="Available for call ?")

def document_upload_path(instance, filename):
    return f'application-docs/{instance.user.username}/{filename}'
class Document(ResumeBaseModel):
    DOC_TYPES = (
        ('resume', 'Resume'),
        ('cv', 'Curriculum Vitae'),
        ('Academic', 'Certificates')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")
    doc_type = models.CharField(max_length=20, choices=DOC_TYPES, default='resume', verbose_name="Document Type")
    doc_name = models.CharField(max_length=40, verbose_name="Document Name")
    file = models.FileField(upload_to=document_upload_path, verbose_name="Document(PDF)")