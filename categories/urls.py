from django.urls import path
from . views import category_form_creating, showing_all_category
 
urlpatterns = [
    path('create_category/',category_form_creating, name="category_create"),
    path('showing_categories/', showing_all_category, name="category_show"),
]
