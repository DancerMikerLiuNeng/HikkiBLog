from django.contrib import admin

# Register your models here.
from blog.models import Post,InlineImage
from django.db import models


class TinyMCEAdmin(admin.ModelAdmin):
        class Media:
                js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas.js',)

admin.site.register(Post,TinyMCEAdmin)
admin.site.register(InlineImage)
