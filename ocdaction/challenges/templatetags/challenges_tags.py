from django import template

register = template.Library()

@register.simple_tag
def render_anxiety_level(score):
    if score:
        anxiety_level = score
    else:
        anxiety_level = "-"
    return anxiety_level

@register.simple_tag
def get_anxiety_level(challenge):
    anxiety_level = challenge.get_latest_initial_anxiety_level()
    if anxiety_level == -1:
        return "-"
    else:
        return anxiety_level
