from datetime import datetime
from django.http import QueryDict
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Event, Speaker


class ScheduleView(TemplateView):
    template_name = "core/schedule.html"


def index(request):
    """
    Return the page view with the contexts of the data.
    """
    speakers = Speaker.objects.all()
    day_1 = Event.objects.all().filter(date=datetime(2022, 6, 6))
    day_2 = Event.objects.all().filter(date=datetime(2022, 6, 7))
    day_3 = Event.objects.all().filter(date=datetime(2022, 6, 8))
    day_4 = Event.objects.all().filter(date=datetime(2022, 6, 9))
    day_5 = Event.objects.all().filter(date=datetime(2022, 6, 10))
    day_6 = Event.objects.all().filter(date=datetime(2022, 6, 11))
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
                  })


class AboutView(TemplateView):
    template_name = "core/about.html"


class SpeakerView(TemplateView):
    template_name = "core/speaker.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"
