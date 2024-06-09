from django.shortcuts import render,redirect
from meetups.models import Meetups,Participant

from .forms import RegistrationForm

# Create your views here.

def meetup_list(request):
    meetups = Meetups.objects.all()
    return render(request,'meetups/meetups.html',{
        'meetups': meetups
    })

def meetup_detail(request, meetup_slug):
    try:
        meetup = Meetups.objects.get(slug = meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant,_ = Participant.objects.get_or_create(email=user_email)
                meetup.participant.add(participant)
                return redirect('confirmation',meetup_slug = meetup_slug)

        return render(request, "meetups/meetup_detail.html",{
            'meetup_found':True,
            'meetup':meetup,
            'page_title': meetup.title,
            'form': registration_form
        })
    except Exception as exc:
        print(exc)
        return render(request,"meetups/meetup_detail.html",{
            'meetup_found' : False,
            'page_title': 'meetup-not-found',
        })

def confirmation(request,meetup_slug):
    meetup = Meetups.objects.get(slug = meetup_slug)
    context = {
        'organizer_email': meetup.organizer
    }
    return render(request, "meetups/confirmation.html",context)
