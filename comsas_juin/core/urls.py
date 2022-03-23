from django.urls import path, include
from core.views import IndexView, SpeakerView, ContactView, SheduleView
app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('speakers/', SpeakerView.as_view(), name='speakers'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('shedule', SheduleView.as_view(), name='shedule'),
    
]
