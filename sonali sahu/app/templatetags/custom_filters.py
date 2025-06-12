# your_app/templatetags/custom_filters.py
from django import template
import re

register = template.Library()

@register.filter
def first_sentence(text):
    # Use regex to capture everything before the first period or full stop
    match = re.match(r"^(.*?[\.\?!])", text)
    if match:
        return match.group(0).strip()
    return text
