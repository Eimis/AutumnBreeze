from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    '''
    retrieves dict value by key lookup in Django template
    '''
    return dictionary.get(key)
