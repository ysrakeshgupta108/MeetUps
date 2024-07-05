from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Meetup, Participant
from .forms import RegistrationForm
# Create your views here.

def index(request):
    meetups = Meetup.objects.all().order_by('id')
    print(meetups)
    return render(request, "meetups/index.html", {"meetups": meetups})


def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = get_object_or_404(Meetup, slug=meetup_slug)
    print(selected_meetup)
    print(request.method)
    if request.method=="GET":
        registration_form = RegistrationForm()
    else:
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user_email  = registration_form.cleaned_data['email']
            user, was_created = Participant.objects.get_or_create(email=user_email, name=registration_form.cleaned_data['name'])
            selected_meetup.participants.add(user)
            return redirect('registeration-success', slug=meetup_slug)


    return render(request, "meetups/meetup_details.html", {
        "selected_meetup": selected_meetup,
        "form": registration_form})

def registration_confirmation(request, slug):
    selected_meetup = get_object_or_404(Meetup, slug=slug)
    print(selected_meetup)
    return render(request, "meetups/registration_success.html", {"selected_meetup": selected_meetup})