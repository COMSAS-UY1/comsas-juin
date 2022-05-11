from email import message
import imp
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, View

from core.forms import ContactRequestForm
from .models import Edition, Event, Journey, Partner, Slider, Person
from django.contrib import messages


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


class AboutView(View):
    template_name = "core/about.html"

    def get(self, request, *args, **kwargs):
        # get curret edition
        current_edition = get_object_or_404(Edition, status="active")
        # Speakers context data
        speakers = current_edition.persons.filter(role="Organizer").order_by("full_name")
        return render(
            request,
            self.template_name,
            context={
                "speakers": speakers,
            },
        )


class SpeakerView(View):
    template_name = "core/speaker.html"

    def get(self, request, *args, **kwargs):
        # get curret edition
        current_edition = get_object_or_404(Edition, status="active")
        # Speakers context data
        speakers = current_edition.persons.filter(role="Speaker").order_by("full_name")
        return render(
            request,
            self.template_name,
            context={
                "speakers": speakers,
            },
        )


class SolutionChallengeView(TemplateView):
    template_name = "core/sc.html"


class TimeLineView(TemplateView):
    template_name = "core/time-line.html"


class ContactView(View):
    template_name = "core/contact.html"
    form_class = ContactRequestForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            contact_request = form.save()
            # mail_subject = _('Nouvel avis sur votre site')
            # html_message = render_to_string(
            #     'core/email_messages.html', {
            #         'email': contact_request.email,
            #         'name': contact_request.name,
            #         'numero': contact_request.numero,
            #         'message': contact_request.message,
            #         'domain': current_site
            #     })
            # plain_message = strip_tags(html_message)

            # try:
            #     send_mail(mail_subject,
            #               plain_message,
            #               None,
            #               fail_silently=False,
            #               recipient_list=['yannik.kadjie@facsciences-uy1.cm'],
            #               html_message=html_message)
            # except BadHeaderError:
            #     messages.error(_('Invalid header found. Please retry later'))
            #     return render(request, self.template_name, {
            #         'form': form,
            #     })
            messages.success(request, ("Your message has been successfully sent"))
            return redirect("core:home")

        return render(
            request,
            self.template_name,
            {
                "form": form,
            },
        )
