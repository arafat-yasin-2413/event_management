from django import forms 
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        
        
        labels = {
            'name' : 'Event Name :',
            'description': 'Event Description',
            'date': 'Event Date',
            'time': 'Event Time',
            'location': 'Event Location',
            'category': 'Select Category',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-md focus:outline-none border ',
                'placeholder':'enter event name', 
            }),
            
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 rounded-md focus:outline-none border ',
                'placeholder': 'write event description',
                'rows': 4, 
            }),
            
            'date': forms.DateInput(attrs= {
                'class': 'w-full p-2 rounded-md focus:outline-none border ',
                'type':'date',
            }),
            
            'time': forms.TimeInput(attrs={
                'class': 'w-full p-2 rounded-md focus:outline-none border ',
                'type': 'time',
            }),
            
            'location': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-md focus:outline-none border ',
                'placeholder': 'write event location',
                
            }),
            
            'category': forms.Select(attrs={
                'class': 'w-full p-2 rounded-md focus:outline-none border ', 
            }),
            
        }