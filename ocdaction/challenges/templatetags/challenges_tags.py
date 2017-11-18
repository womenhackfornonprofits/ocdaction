from django import template
from ..models import Challenge, AnxietyScoreCard

register = template.Library()

@register.simple_tag
def get_anxiety_level(challenge):
    try:
        anxiety_score_card = AnxietyScoreCard.objects.filter(challenge=challenge).last()
        anxiety_level = anxiety_score_card.anxiety_at_0_min
    except:
        AnxietyScoreCard.DoesNotExist
        anxiety_level = "-"
    return anxiety_level
