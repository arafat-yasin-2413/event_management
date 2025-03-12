from django.shortcuts import render, redirect
from . forms import ParticipantForm


# Create your views here.

def participant_form_creating(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_create')
    else:
        form = ParticipantForm()
    return render(request, 'participants/participants_form.html', {'form':form})

