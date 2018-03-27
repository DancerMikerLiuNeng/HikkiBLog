from django.db import models
from django.utils.encoding import smart_unicode
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    tags = TaggableManager()
    
    def __unicode__(self):
        return smart_unicode(self.title)
    
    
class InlineImage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    title = models.CharField(max_length=100)
    image           = models.ImageField(upload_to='uploads/images')
    identifier      = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.title
        ordering = ('-created',)