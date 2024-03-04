from django.contrib import admin
from .models import Agent,Property,Client,Request

admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(Client)
admin.site.register(Request)