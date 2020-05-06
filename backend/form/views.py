from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import TrialClass,Slots
from .forms import TrialClassForm
from datetime import datetime,timedelta,date

class TrialClassCreateView(CreateView):
    model = TrialClass
    form_class = TrialClassForm
    success_url = reverse_lazy('trialclass_changelist')


def load_slots(request):
    course_id = request.GET.get('course')
    time_gap = (datetime.today()+timedelta(days=5))
    slots = Slots.objects.filter(course_id=course_id)
    slots_within_range = slots.filter(slot_date__lte=time_gap)
    
    return render(request, 'form/city_dropdown_list_options.html', {'slots': slots_within_range})