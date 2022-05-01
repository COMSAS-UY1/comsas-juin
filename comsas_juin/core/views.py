from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Event, Partner, Slider, Speaker


class ScheduleView(TemplateView):
    template_name = "core/schedule.html"


def index(request):
    """
    Return the page view with the contexts of the data.
    """
    # Speakers context data
    speakers = Speaker.objects.all()
    # Programs/Events context data
    day_1 = Event.objects.all().filter(date=datetime(2022, 6, 6))
    day_2 = Event.objects.all().filter(date=datetime(2022, 6, 7))
    day_3 = Event.objects.all().filter(date=datetime(2022, 6, 8))
    day_4 = Event.objects.all().filter(date=datetime(2022, 6, 9))
    day_5 = Event.objects.all().filter(date=datetime(2022, 6, 10))
    day_6 = Event.objects.all().filter(date=datetime(2022, 6, 11))
    # Sliders context data
    sliders = Slider.objects.all()
    # Partners context data
    partners = Partner.objects.all()
    return render(request,
                  "core/index.html",
                  context={
                      'speakers': speakers,
                      'day_1': day_1,
                      'day_2': day_2,
                      'day_3': day_3,
                      'day_4': day_4,
                      'day_5': day_5,
                      'day_6': day_6,
                      'sliders': sliders,
                      'partners': partners,
                  })


class AboutView(TemplateView):
    template_name = "core/about.html"


class SpeakerView(TemplateView):
    template_name = "core/speaker.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"


class SolutionChallengeView(TemplateView):
    template_name = "core/solution.html"