from django.urls import path
from . views import category_form_creating
 
urlpatterns = [
    path('create_category/',category_form_creating, name="category_create"),
    
]
