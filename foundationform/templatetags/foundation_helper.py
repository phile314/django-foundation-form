from django.template import Library

register = Library()

@register.filter
def addclass(field, cls):
  return field.as_widget(attrs={"class":cls})


