from django.shortcuts import render, redirect
from . forms import ParticipantForm
from . models import Participant

# Create your views here.

def participant_creating_form(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_create')
    else:
        form = ParticipantForm()
    return render(request, 'participants/participants_form.html', {'form':form})



def showing_participants(request):
    participants = Participant.objects.all()
    return render(request,'participants/participants_form.html', {'participants':participants})



def update_participant(request, id):
    participant = Participant.objects.get(pk = id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_create')
    else:
        form = ParticipantForm(instance=participant)
    return render(request,'participants/participants_form.html', {'form':form})


def delete_participant(request,id):
    participant = Participant.objects.get(pk = id)
    if request.method == 'POST':
        participant.delete()
        return redirect ('participant_create')
    return render(request,'participants/participant_delete.html', {'participant':participant})

