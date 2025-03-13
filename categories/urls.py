from django.urls import path
from . views import category_form_creating, showing_all_category
from . views import update_category, delete_category
urlpatterns = [
    path('create/',category_form_creating, name="category_create"),
    path('show/', showing_all_category, name="category_show"),
    path('update/<int:id>/',update_category, name="category_update"),
    path('delete/<int:id>/', delete_category, name="category_delete"),
    
    
    
]
