from django.contrib import admin
from log.models import Log, Event

class LogAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'description')

class EventAdmin(admin.ModelAdmin):
    list_display = ('log', 'time', 'data')

admin.site.register(Log, LogAdmin)
admin.site.register(Event, EventAdmin)

