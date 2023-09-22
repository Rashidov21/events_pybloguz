from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Tag)
admin.site.register(Speaker)
admin.site.register(Event)
admin.site.register(Leads)