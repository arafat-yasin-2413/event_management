from django.urls import path
from .views import participant_form_creating

urlpatterns = [
    path('participant_creating/', participant_form_creating, name="participant_create"),
    
    
    
]
