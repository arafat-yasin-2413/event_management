from django.urls import path
from .views import event_form_creating

urlpatterns = [
    path('create_event/',event_form_creating, name="event_create"),
    
]
