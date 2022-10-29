from django.contrib import admin
from jobs.models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'apply_by', 'created', 'updated']
    list_filter = ['apply_by',]
    search_fields = ['title', 'requirements']
    # prepopulated_fields = {'slug': ['title'],}

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant','parent_job', 'status', 'created']