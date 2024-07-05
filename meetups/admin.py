from django.contrib import admin
from .models import Meetup, Location, Participant
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title','slug','meetLocation', 'organizer_email','date')
    list_filter = ('meetLocation','organizer_email')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
