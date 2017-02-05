from django.contrib import admin
from .models import Task, AnxietyScore


class TaskAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('task_name', 'user')
    search_fields = ['task_name']


class AnxietyScoreAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('user', 'task', 'score')
    search_fields = ['task__task_name']


# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(AnxietyScore, AnxietyScoreAdmin)
