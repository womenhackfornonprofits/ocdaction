from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('taskname', 'user')
    search_fields = ['taskname']

# Register your models here.
admin.site.register(Task, TaskAdmin)