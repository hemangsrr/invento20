from django.contrib import admin
from .models import Event, Event_register, Ambassador
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', '_type', 'fee', 'prize', 'day','short_desc')#,'long_desc','imageurl','posterurl')
    list_filter = ('category', '_type', 'fee', 'prize')

class Event_registerResource(resources.ModelResource):
    class Meta:
        model = Event_register
        
@admin.register(Event_register)
class Event_registerAdmin(ImportExportModelAdmin):
    resource_class = Event_registerResource
    list_display = ('first_name', 'college', 'email', 'phone', 'referal_code', 'event')
    list_filter = ('referal_code', 'event')

@admin.register(Ambassador)
class Ambassador_registerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone','college','department', 'referal_code')
