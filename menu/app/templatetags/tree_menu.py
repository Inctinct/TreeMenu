from django import template
from django.http import HttpRequest
from django.template import RequestContext
from django.urls import reverse, NoReverseMatch
from ..models import TreeMenu

register = template.Library()


@register.inclusion_tag('app/menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str = '', parent: int = 0):

    if parent != 0 and 'menu' in context:
        menu = context['menu']
    else:
        data = TreeMenu.objects.filter(main_menu__name=name).order_by('pk')
        current_path = context['request'].path \
            if 'request' in context and isinstance(context['request'], HttpRequest) \
            else ''
        menu = []
        for item in data:
            try:
                url = reverse(item.path)
            except NoReverseMatch:
                url = item.path
            menu.append({
                'id': item.pk,
                'url': url,
                'name': item.name,
                'parent': item.parent_id or 0,
                'active': True if url == current_path else False,
            })
    return {
        'menu': menu,
        'current_menu': (item for item in menu if 'parent' in item and item['parent'] == parent),
    }

