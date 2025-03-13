from django import forms 
from . models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"
        
        labels = {
            'name': 'Name:',
            'email': 'Email',
            'event': 'Event',
        }
        
        
        widgets = {
            'name': forms.TextInput(attrs= {
                'class': 'w-full p-2 rounded-md focus:outline-none border ',
                'placeholder':'type your name',
            }),
            
            'email': forms.EmailInput(attrs={
                'class':'w-full p-2 rounded-md focus:outline-none border ',
                'placeholder':'type your email',
            }),
            
            'event': forms.CheckboxSelectMultiple(attrs={
               'class' : 'w-full p-2 rounded-md focus:outline-none border ' 
            }),
                
        }
        
