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
        'anxiety_at_0_min',
        'anxiety_at_5_min',
        'anxiety_at_10_min',
        'anxiety_at_15_min',
        'anxiety_at_30_min',
        'anxiety_at_60_min',
        'anxiety_at_120_min'
    )
    search_fields = ['challenge__challenge_name']


# Register your models here.
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(AnxietyScoreCard, AnxietyScoreCardAdmin)
