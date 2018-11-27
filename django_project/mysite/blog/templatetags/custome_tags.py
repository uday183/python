from django import template
register = template.Library()


@register.simple_tag
def any_function(request):
  	return {'ab':[12,24,5,6]}



 
