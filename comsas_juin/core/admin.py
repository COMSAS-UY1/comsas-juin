from django.contrib import admin
from .models import Edition, Event, Partner, Slider, Speaker


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'directed_by')
    list_filter = ('date', 'directed_by__full_name')


admin.site.register(Edition)
admin.site.register(Speaker)
admin.site.register(Event, EventAdmin)
admin.site.register(Partner)
admin.site.register(Slider)
