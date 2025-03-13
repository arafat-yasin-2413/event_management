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


