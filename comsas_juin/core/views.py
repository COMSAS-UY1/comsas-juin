from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Event, Journey, Partner, Slider, Speaker


class ScheduleView(TemplateView):
    template_name = "core/schedule.html"


class IndexView(View):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        # Speakers context data
        speakers = Speaker.objects.all()
        # Journeys context data
        journeys = Journey.objects.all().order_by("date")
        # Events context data
        events = Event.objects.all().order_by("start_time")
        # Sliders context data
        sliders = Slider.objects.all()
        # Partners context data
        partners = Partner.objects.all()
        return render(
            request,
            self.template_name,
            context={
                "speakers": speakers,
                "journeys": journeys,
                "events": events,
                "sliders": sliders,
                "partners": partners,
            },
        )


class AboutView(TemplateView):
    template_name = "core/about.html"


class SpeakerView(View):
    template_name = "core/speaker.html"

    def get(self, request, *args, **kwargs):
        # Speakers context data
        speakers = Speaker.objects.all()

        return render(
            request,
            self.template_name,
            context={
                "speakers": speakers,
            },
        )


class ContactView(TemplateView):
    template_name = "core/contact.html"


class SolutionChallengeView(TemplateView):
    template_name = "core/solution.html"


class TimeLineView(TemplateView):
    template_name = "core/time_line.html"
