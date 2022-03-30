from django.shortcuts import render
import os
import psycopg2.extras
from servers.models import Server
from .models import ServerWiki


def wiki(request, page_alias):    
    server_object = Server.objects.get(server_name=page_alias)
    wiki_object = ServerWiki.objects.get(id=server_object.wiki_id)
    
    context = {}
    
    context['server'] = server_object
    context['wiki'] = wiki_object
  

    return render(request, 'wiki_page.html', context)


def connection(request, page_alias):
    server_object = Server.objects.get(server_name=page_alias)
    wiki_object = ServerWiki.objects.get(id=server_object.wiki_id)
    
    
    context = {}
        
    context['server'] = server_object
    context['wiki'] = wiki_object
  

    return render(request, 'connection_page.html', context)