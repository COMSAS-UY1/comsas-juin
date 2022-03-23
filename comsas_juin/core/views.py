from django.shortcuts import render
from django.views.generic import TemplateView


class SheduleView(TemplateView):
    template_name = "core/shedule.html"


class IndexView(TemplateView):
    template_name = "core/index.html"


class aboutView(TemplateView):
    template_name = "core/about.html"


class SpeakerView(TemplateView):
    template_name = "core/speaker.html"

class ContactView(TemplateView):
    template_name = "core/contact.html"
