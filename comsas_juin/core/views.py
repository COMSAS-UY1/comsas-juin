from django.shortcuts import render
from django.views.generic import TemplateView


class ScheduleView(TemplateView):
    template_name = "core/schedule.html"


class IndexView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class SpeakerView(TemplateView):
    template_name = "core/speaker.html"

class ContactView(TemplateView):
    template_name = "core/contact.html"
