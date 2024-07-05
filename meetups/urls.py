from django.urls import path, include
from . import views
urlpatterns = [
    path('meetups/', views.index,name='all-meetups'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meet-detail'),
    path('meetups/success/<str:slug>',views.registration_confirmation, name="registeration-success")
]
