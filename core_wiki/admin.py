from django.contrib import admin
from .models import ServerWiki


class WikiAdmin(admin.ModelAdmin):
    def __init__(self, *args):
        super(WikiAdmin, self).__init__(*args)
        
    list_display = ('title', 'updated_at')
    search_fields = ['title', 'updated_at', 'wikiPage',]
    
admin.site.register(ServerWiki, WikiAdmin)