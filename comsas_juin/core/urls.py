from django.urls import path, include
from core.views import IndexView, SpeakerView, ContactView, ScheduleView, AboutView
app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('speakers', SpeakerView.as_view(), name='speakers'),
    path('contact', ContactView.as_view(), name='contact'),
    path('schedule', ScheduleView.as_view(), name='schedule'),
    path('about', AboutView.as_view(), name='about'),
    
]
