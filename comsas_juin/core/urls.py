from django.urls import path
from core.views import SpeakerView, ContactView, ScheduleView, AboutView, index
app_name = 'core'

urlpatterns = [
    path('', index, name='home'),
    path('speakers', SpeakerView.as_view(), name='speakers'),
    path('contact', ContactView.as_view(), name='contact'),
    path('schedule', ScheduleView.as_view(), name='schedule'),
    path('about', AboutView.as_view(), name='about'),
    
]
