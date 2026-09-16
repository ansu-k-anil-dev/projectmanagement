from django import template

register = template.Library()

@register.filter(name='get_item')
def get_eval(evaluations, group_id):
    """
    Custom template filter to get evaluation data for a specific group
    Usage: {{ evaluations|get_item:group.id }}
    """
    return evaluations.get(group_id)