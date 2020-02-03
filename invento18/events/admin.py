from django.contrib import admin
from .models import Event, Event_register
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', '_type', 'fee','imageurl','short_desc','long_desc', 'prize', 'day')
    list_filter = ('category', '_type', 'fee', 'prize')

@admin.register(Event_register)
class Event_registerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'referal_code','event')
