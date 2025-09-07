from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name: str, css_on="bg-gray-100 text-blue-700", css_off=""):
    """
    Uso: class="{% active 'home' %}"
    """
    try:
        current = context["request"].resolver_match.url_name
        return css_on if current == url_name else css_off
    except Exception:
        return css_off