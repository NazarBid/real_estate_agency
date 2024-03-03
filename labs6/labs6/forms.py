from django import forms
from .models import Agent, Property, Client, Request

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'specialty']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['type', 'address', 'price', 'agent']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'contact_email']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['client', 'property']
