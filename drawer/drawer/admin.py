from django.contrib import admin

from .models import Plan, Project


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass