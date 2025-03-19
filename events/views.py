from django.shortcuts import render, redirect
from . forms import EventForm
from . models import Event

# Create your views here.

def event_form_creating(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_create')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form':form})





def showing_events(request):
    events = Event.objects.all()
    return render(request,'events/event_form.html', {'events':events})



def update_event(request, id):
    event = Event.objects.get(pk = id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_create')
    else:
        form = EventForm(instance=event)
    return render(request,'events/event_form.html', {'form':form})


def delete_event(request,id):
    event = Event.objects.get(pk = id)
    if request.method == 'POST':
        event.delete()
        return redirect ('event_create')
    return render(request,'events/event_delete.html', {'event':event})

