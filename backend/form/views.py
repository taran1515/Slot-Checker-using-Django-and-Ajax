from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import TrialClass,Slots,TimeSlots
from .forms import TrialClassForm
from datetime import datetime,timedelta,date


def trialclasscreate(request):
    if request.method == 'POST':
        form = TrialClassForm(request.POST)
        if form.is_valid():
            print("go")
            form.save(commit=True)
            form = TrialClassForm()
        else:
            print("stop")
            print (form.errors)
    else:
        form = TrialClassForm()
    return render(request, 'form/trialclass_form.html', {'form': form})

def load_slots(request):
    course_id = request.GET.get('course')
    time_gap = (datetime.today()+timedelta(days=5))
    slots = Slots.objects.filter(course_id=course_id)
    slots_within_range = slots.filter(slot_date__lte=time_gap)
    return render(request, 'form/date_options.html', {'slots': slots_within_range})

def load_time_slots(request):
    slot_id = request.GET.get('slot')
    time_gap2 = datetime.now()+timedelta(hours=4)
    slots = TimeSlots.objects.filter(slot_id=slot_id)
    slots_within_time_range = slots.filter(time_slot__gte=time_gap2)
    return render(request, 'form/time_options.html', {'slots': slots_within_time_range})