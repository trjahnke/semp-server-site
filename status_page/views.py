from django.shortcuts import render
from django.http import HttpResponse
import os
import psycopg2.extras


def landing(request):
    
    try:
        conn = psycopg2.connect(database=os.environ['DJANGO_DB_NAME'], user=os.environ['DB_USER'],
                            password=os.environ['DB_PASSWORD'], host=os.environ['DB_HOST'], port=os.environ['DB_PORT'])   
        message = "Connected to the database"
    except:
        message = "Failed to connected to the database"
    
    # Get servers from DB
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM servers_server")
    servers = cur.fetchall()
    context = {}

    for server in servers:
        response = os.system("ping -c 1 " + server['url'])        
        context[server['server_name']] = response

      
    
    context['servers'] = servers
    conn.close()

    return render(request, 'landing.html', context)

