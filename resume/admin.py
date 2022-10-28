from django.contrib import admin

from resume.models import Document, Education, Experience, Referee


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['user', 'institution_name', 'course', 'grade']
    list_filter = ['enrolled', 'created', 'updated']
    search_fields = ['institution_name', 'course', 'grade']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'organization_name', 'position', 'in_role']
    list_filter = ['created', 'updated']
    search_fields = ['user', 'position', 'description']

@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ['user', 'referee_name', 'phone', 'email']
    list_filter = ['call',]
    search_fields = ['user',]

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['user', 'doc_type', 'doc_name', 'created']
    search_fields = ['user', 'doc_type', 'doc_name']
    list_filter = ['doc_type', 'created', 'updated']