from django.contrib import admin
from .models import Task, AnxietyScore, AnxietyScoreCard


class TaskAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('task_name', 'user')
    search_fields = ['task_name']


class AnxietyScoreAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('user_name', 'task', 'score')
    search_fields = ['task__task_name']


class AnxietyScoreCardAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('task', 'user_name', 'score_after_5_min', 'score_after_10_min', 'score_after_15_min', 'score_after_20_min')
    search_fields = ['task__task_name']


# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(AnxietyScore, AnxietyScoreAdmin)
admin.site.register(AnxietyScoreCard, AnxietyScoreCardAdmin)
