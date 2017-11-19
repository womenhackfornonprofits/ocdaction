from django import template
from ..models import Challenge, AnxietyScoreCard

register = template.Library()

@register.simple_tag
def render_anxiety_level(score):
    if score:
        anxiety_level = score
    else:
        anxiety_level = "-"
    return anxiety_level
