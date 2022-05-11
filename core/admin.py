from django.contrib import admin
from .models import Edition, Event, Journey, Partner, Slider, Person, SpeakerEvent


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date",
    )
    list_filter = ("date__date",)


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "role",
    )
    list_filter = ("role",)


admin.site.register(Edition)
admin.site.register(Journey)
admin.site.register(Person, PersonAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Partner)
admin.site.register(Slider)
admin.site.register(SpeakerEvent)
