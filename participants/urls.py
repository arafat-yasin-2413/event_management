from django.urls import path
from .views import participant_creating_form, showing_participants
from . views import update_participant, delete_participant


urlpatterns = [
    path('create/', participant_creating_form, name="participant_create"),
    path('show/',showing_participants, name="participant_show"),
    path('update/<int:id>/', update_participant, name="participant_update"),
    path('delete/<int:id>/', delete_participant, name="participant_delete"),
    
    
]
