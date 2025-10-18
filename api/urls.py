from django.urls import path
from . import views

urlpatterns = [
    path('me', views.get_profile, name='get_profile'),
]