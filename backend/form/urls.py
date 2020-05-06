from django.urls import include, path
from . import views

urlpatterns = [
    path('add/', views.TrialClassCreateView.as_view(), name='trialclass_add'),
    path('ajax/load-slots/', views.load_slots, name='ajax_load_slots'),
]