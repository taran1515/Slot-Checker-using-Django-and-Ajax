from django.urls import include, path
from . import views
from datetime import datetime,timedelta 
import requests
from .models import Slots, Course, TimeSlots

urlpatterns = [
    path('add/', views.trialclasscreate, name='trialclass_add'),
    path('ajax/load-slots/', views.load_slots, name='ajax_load_slots'),
    path('ajax/load-time_slots/', views.load_time_slots, name='ajax_load_time_slots'),

]

# def getchoice(j):

#     r = requests.get('https://script.googleusercontent.com/macros/echo?user_content_key=3QIfSWtbjynPofOnfE_8SugMIs8YRFwsbsAXMR-oZBO0goj1E7OjSM0X3RyL6PPBmKhputy-Kxbuz4PaAoWQ5BFhcqqesPwum5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnC09Nb0QZ6ca_LU0vmo6mSiQ7SyFG3CgdL9-1Vgcha-TAYaAGhh-9xNG-9rMNEZHQRElvdDletx0&lib=MlJcTt87ug5f_XmzO-tnIbN3yFe7Nfhi6')
#     Choice =  (r.json()) 
#     course_name = Choice[j]['course_name']
#     x = len(Choice[j]['slots'])
#     date = []
#     time = []
#     for i in range(x):
#         your_dt = datetime.fromtimestamp(int(Choice[j]['slots'][i]['slot'])/1000)
#         slot_date = (your_dt.strftime("%Y-%m-%d"))
#         date.append(slot_date)
#         slot_time = (your_dt.strftime("%H:%M:%S"))
#         time.append(slot_time)
#     course = Course.objects.get(name=course_name)
#     distinct_date = set(date)
    
#     for d in (distinct_date):
#         slot_save = Slots.objects.create(course=course,slot_date=d)
#         print(slot_save)
#         slot_save.save()

#     for i in range(len(time)):
#         print(date[i])
#         print(time[i])
#         slot = Slots.objects.filter(slot_date=date[i])
#         for j in range(len(slot)):
#             time_slot = TimeSlots.objects.create(slot=slot[j],time_slot=time[i])
#             time_slot.save()



# for r in range(5):
#     getchoice(r)