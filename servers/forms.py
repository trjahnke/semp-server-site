from django import forms
from .models import Server


class AddServerForm(forms.ModelForm):
    
    class Meta:
        model = Server
        fields = "__all__"
        