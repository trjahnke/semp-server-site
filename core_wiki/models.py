from django.db import models
from ckeditor.fields import RichTextField

class ServerWiki(models.Model):
    def __init__(self, *args):
        super(ServerWiki, self).__init__(*args)
        
    class Meta:
        verbose_name = "Server Wiki"
        verbose_name_plural = "Server Wiki's"
        
    def __str__(self):
        return self.title
        
    title = models.CharField(max_length=200)
    wikiPage = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)
    
    
