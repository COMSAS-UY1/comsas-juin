from django.contrib import admin
from .models import Edition, Event, Partner, Slider, Speaker


admin.site.register(Edition)
admin.site.register(Speaker)
admin.site.register(Event)
admin.site.register(Partner)
admin.site.register(Slider)
