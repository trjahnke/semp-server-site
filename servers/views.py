from django.shortcuts import render, redirect
from .forms import AddServerForm
from .models import Server
from django.contrib import messages


def ServerForm(request):
    if request.method == 'POST':
        form = AddServerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Server added successfully')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
            
    form = AddServerForm()
    server = Server.objects.all()
    return render(request, 'new_server.html', {'form': form, 'server': server})