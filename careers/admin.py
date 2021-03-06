from django.contrib import admin
from .models import Career, JobDescription

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone', 'email', 'applying_for', 'education','uploaded_at')
    search_fields = ('fullname', 'phone', 'email', 'applying_for', 'education')
    list_filter = ('uploaded_at', )
    ordering = ('uploaded_at',)


@admin.register(JobDescription)
class JobDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'display')


