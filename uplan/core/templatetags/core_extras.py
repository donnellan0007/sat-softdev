import re

from django.utils.safestring import mark_safe
from django import template
register = template.Library()

@register.filter
def highlight_search(text, search):
    highlighted = re.sub('(?i)(%s)' % (re.escape(search)), '<span class="highlight">\\1</span>', text)
    return mark_safe(highlighted)