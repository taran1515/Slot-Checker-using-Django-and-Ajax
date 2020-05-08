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
    """
    Here to show that the latest slot to be fetched 
    upto max. 7 days from now, I have taken 2020-04-27
    as current date. Now it fetches all the days upto 7 
    days from 27th April i.e upto 4th May. All slots with
    dates greater than 4th May is not fetched.
    """
    current_day = datetime.today()-timedelta(days=11)
    time_gap = current_day + timedelta(days=7)
    slots = Slots.objects.filter(course_id=course_id)
    slots_within_range = slots.filter(slot_date__lte=time_gap)
    if slots_within_range is None:
        slots_within_range.slot_date = 'No slot during current day'
    return render(request, 'form/date_options.html', {'slots': slots_within_range})

def load_time_slots(request):
    slot_id = request.GET.get('slot')
    x = Slots.objects.get(id=slot_id)
    # current_day = (datetime.today()).strftime("%Y-%m-%d")
    current_day = (datetime.today()-timedelta(days=4)).strftime("%Y-%m-%d")
    """
    This if statement makes sure that slot date
    is chosen as current date, then time slot should be minimum 4 hours from now
    else retrieve all time slots
    """
    if(str(current_day)==str(x)):
        time_gap2 = datetime.now()+timedelta(hours=4)
        slots = TimeSlots.objects.filter(slot_id=slot_id)
        slots_within_time_range = slots.filter(time_slot__gte=time_gap2)
    else:
        slots_within_time_range = TimeSlots.objects.filter(slot_id=slot_id)

    return render(request, 'form/time_options.html', {'slots': slots_within_time_range})