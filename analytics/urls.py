from django.urls import path

from main import views
from analytics import views



urlpatterns = [

    path('', views.analytics, name='analytics'),

]