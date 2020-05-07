from django.urls import include, path
from . import views

urlpatterns = [
    path('add/', views.trialclasscreate, name='trialclass_add'),
    path('ajax/load-slots/', views.load_slots, name='ajax_load_slots'),
    path('ajax/load-time_slots/', views.load_time_slots, name='ajax_load_time_slots'),

]