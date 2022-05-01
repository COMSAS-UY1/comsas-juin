from django.urls import path
from core.views import SpeakerView, ContactView, ScheduleView, AboutView, IndexView, TimeLineView, SolutionChallengeView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('speakers', SpeakerView.as_view(), name='speakers'),
    path('contact', ContactView.as_view(), name='contact'),
    path('schedule', ScheduleView.as_view(), name='schedule'),
    path('about', AboutView.as_view(), name='about'),
    path('solution_challenge', SolutionChallengeView.as_view(), name='solution_challenge'),
    path('time_line', TimeLineView.as_view(), name='time_line'),
   
]
