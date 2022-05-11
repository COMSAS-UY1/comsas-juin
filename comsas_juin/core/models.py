from asyncio import events
from django.db import models


class Edition(models.Model):
    STATUS = (("programmed", "programmed"), ("active", "active"))
    name = models.CharField(max_length=50, null=False)
    begin_date = models.DateField(null=True, default=None)
    end_date = models.DateField(null=True, default=None)
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return self.name


class Journey(models.Model):
    date = models.DateField()
    is_the_first_date = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)

    def get_event(self):
        return self.events.all().order_by("date")


class Event(models.Model):
    flyers = models.ImageField(upload_to="images/events/")
    location = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.ForeignKey(Journey, models.CASCADE, related_name="events")
    edition = models.ForeignKey(Edition, models.CASCADE, related_name="events")

    def __str__(self):
        return self.title

    def get_speaker(self):
        return SpeakerEvent.objects.filter(event=self.id).order_by("event__date")


class Person(models.Model):
    ROLE = (
        ("Speaker", "speaker"),
        ("Organizer", "organizer"),
        ("Contributor", "contributor"),
    )
    full_name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to="images/speakers/")
    post = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=50, null=True, choices=ROLE)
    email = models.EmailField(null=False, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkdin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    about = models.TextField()
    edition = models.ForeignKey(
        Edition, models.SET_NULL, null=True, blank=True, related_name="persons"
    )

    def __str__(self):
        return self.full_name


class SpeakerEvent(models.Model):
    event = models.ForeignKey(Event, models.CASCADE)
    speaker = models.ForeignKey(Person, models.CASCADE)


class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="images/partners/")
    web_site = models.URLField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField()
    edition = models.ForeignKey(Edition, models.CASCADE, related_name="partners")

    def __str__(self):
        return self.name


class Slider(models.Model):
    big_title = models.CharField(max_length=255, null=False)
    small_title = models.CharField(max_length=255)
    background = models.ImageField(upload_to="images/slides/")

    def __str__(self):
        return self.big_title


class ContactRequest(models.Model):  # laisser un messages aux admins
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=15)
    date_sended = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.name}"
