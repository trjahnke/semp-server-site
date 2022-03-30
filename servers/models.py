from django.db import models
from core_wiki.models import ServerWiki


class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()
        
        

class Server(models.Model):
    def __init__(self, *args):
        super(Server, self).__init__(*args)
        
    def __str__(self):
        return self.server_name
        
    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Servers"
        
    server_name = NameField(max_length=200)
    url = models.URLField(max_length=200)
    port = models.IntegerField()
    password = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    alt_image = models.CharField(max_length=100)
    description = models.TextField()
    wiki = models.ForeignKey(ServerWiki, default=None, on_delete=models.CASCADE)
