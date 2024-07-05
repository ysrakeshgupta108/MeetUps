from django.db import models
# Create your models here.
from datetime import date

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} {self.address}"

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name}({self.email})"

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField(default="ysrakeshgupta@gmail.com")
    date = models.DateField(default=date.today())
    showMeetups = models.BooleanField(default=True)
    slug =  models.SlugField(unique=True)
    location = models.CharField(max_length=100, default="New York")
    description = models.TextField()
    image = models.ImageField(upload_to='images', null=True)
    meetLocation = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="meetsup", null=True)
    participants = models.ManyToManyField(Participant, null=True, blank=True)

    def __str__(self):
        return f"{self.title} in {self.location }/ {self.meetLocation}"
