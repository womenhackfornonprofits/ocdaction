from django.contrib import admin
from .models import Task, AnxietyScore


class TaskAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('taskname', 'user')
    search_fields = ['taskname']

class AnxietyScoreAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('user','task', 'score')
    search_fields = ['task__taskname']

# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(AnxietyScore, AnxietyScoreAdmin)