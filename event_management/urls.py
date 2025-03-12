from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('events/', include('events.urls')),
    path('categories/', include('categories.urls')),
    path('participants/', include('participants.urls')),
    
]
