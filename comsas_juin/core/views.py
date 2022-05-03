from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, View
from .models import Edition, Event, Journey, Partner, Slider, Person


class ScheduleView(View):
    template_name = "core/schedule.html"

    def get(self, request, *args, **kwargs):
        # Journeys context data
        journeys = Journey.objects.all().order_by("date")
        return render(
            request,
            self.template_name,
            context={
                "journeys": journeys,
            },
        )


class IndexView(View):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        # get curret edition
        current_edition = get_object_or_404(Edition, status="active")
        # Speakers context data
        speakers = current_edition.persons.filter(role="Speaker")
        print(speakers)
        # Journeys context data
        journeys = Journey.objects.all().order_by("date")
        # Events context data
        events = current_edition.events.all().order_by("start_time")
        # Sliders context data
        sliders = Slider.objects.all()
        # Partners context data
        partners = current_edition.partners.all()
        return render(
            request,
            self.template_name,
            context={
                "speakers": speakers,
                "journeys": journeys,
                "events": events,
                "sliders": sliders,
                "partners": partners,
                "organizers": current_edition.persons.filter(role="Organizer"),
            },
        )


class AboutView(TemplateView):
    template_name = "core/about.html"


class SpeakerView(View):
    template_name = "core/speaker.html"

    def get(self, request, *args, **kwargs):
        # get curret edition
        current_edition = get_object_or_404(Edition, status="active")
        # Speakers context data
        speakers = current_edition.persons.filter(role="Speaker")
        # Journeys context data
        journeys = Journey.objects.all().order_by("date")
        return render(
            request,
            self.template_name,
            context={
                "speakers": speakers,
                "journeys": journeys,
            },
        )


class ContactView(TemplateView):
    template_name = "core/contact.html"


class SolutionChallengeView(TemplateView):
    template_name = "core/solution.html"


class TimeLineView(TemplateView):
    template_name = "core/time-line.html"
