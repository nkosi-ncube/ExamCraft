from django.urls import path
from . import views
from .views import home

# This creates a new URL pattern for the quote_of_the_day view. 

urlpatterns = [
    path("",home),
]
