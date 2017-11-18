from django import template
from ..models import Challenge, AnxietyScoreCard

register = template.Library()

@register.simple_tag
def get_anxiety_level(challenge):
    anxiety_level = challenge.get_latest_initial_anxiety_level()
    if anxiety_level == -1:
        return "-"
    else:
        return anxiety_level
