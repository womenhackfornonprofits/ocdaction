from django.contrib import admin
from .models import Challenge, AnxietyScoreCard


class ChallengeAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('challenge_name', 'user')
    search_fields = ['challenge_name']


class AnxietyScoreCardAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = (
        'challenge',
        'user_name',
        'score_after_0_min',
        'score_after_5_min',
        'score_after_10_min',
        'score_after_15_min',
        'score_after_30_min',
        'score_after_60_min'
    )
    search_fields = ['challenge__challenge_name']


# Register your models here.
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(AnxietyScoreCard, AnxietyScoreCardAdmin)
