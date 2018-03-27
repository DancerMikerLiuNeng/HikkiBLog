import re

from django import template
from django.template.defaultfilters import stringfilter

from sorl.thumbnail import get_thumbnail

from blog.models  import InlineImage

register = template.Library()

regex = re.compile(r'\[thumbnail (?P<identifier>[\-\w]+)\]')

@register.filter
@stringfilter
def inline_thumbnails(value):
    new_value= value
    it = regex.finditer(value)
    #img_id_list = re.findall(r'[^\s]+(?=])',value)
    #for img_id in img_id_list:
    for m in it:
        
        try:
            image = InlineImage.objects.get(identifier=m.group().split()[1][:-1])
            #print image.image
            thumbnail = get_thumbnail(image.image,'700x700')
            #print thumbnail.url
            #new_value = '<img src="{}">'.format(thumbnail.url)
            new_value = new_value.replace(m.group(),'<img src="/static{0}">'.format(thumbnail.url))
        except InlineImage.DoesNotExist:
            pass
        print new_value
    return new_value
