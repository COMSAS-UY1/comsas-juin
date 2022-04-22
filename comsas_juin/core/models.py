from django.db import models


class Edition(models.Model):
    STATUS = (("programmed", "programmed"), ("active", "active"))
    name = models.CharField(max_length=50, null=False)
    begin_date = models.DateField(null=True, default=None)
    end_date = models.DateField(null=True, default=None)
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return self.name


class Speaker(models.Model):
    full_name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to="speakers/")
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkdin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    about = models.TextField()
    edition = models.ForeignKey(Edition, models.CASCADE)

    def __str__(self):
        return self.full_name


class Event(models.Model):
    flyers = models.ImageField(upload_to="events/")
    location = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    directed_by = models.ForeignKey(Speaker, models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    edition = models.ForeignKey(Edition, models.CASCADE)

    def __str__(self):
        return self.title


class Partner(models.Model):

    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="Client", default="Client/no_picture.png")
    web_site = models.URLField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField()
    edition = models.ForeignKey(Edition, models.CASCADE)

    def __str__(self):
        return self.name
