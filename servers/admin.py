from django.contrib import admin
from .models import Server


class ServerAdmin(admin.ModelAdmin):
    def __init__(self, *args):
        super(ServerAdmin, self).__init__(*args)
        
    list_display = ['server_name', 'url', 'port', 'description']
    list_filter = ['server_name',]
    search_fields = ['server_name', 'url', 'port', 'description', 'wikiPage']

admin.site.register(Server, ServerAdmin)