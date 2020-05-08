# import requests
# import datetime

# from django.conf import settings
# import backend.settings as app_settings

# if not settings.configured:
#     settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS,DATABASES=app_settings.DATABASES)

# import django
# django.setup()

# from form.models import Course, TrialClass, TimeSlots

# def getchoice():

#     r = requests.get('https://script.googleusercontent.com/macros/echo?user_content_key=3QIfSWtbjynPofOnfE_8SugMIs8YRFwsbsAXMR-oZBO0goj1E7OjSM0X3RyL6PPBmKhputy-Kxbuz4PaAoWQ5BFhcqqesPwum5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnC09Nb0QZ6ca_LU0vmo6mSiQ7SyFG3CgdL9-1Vgcha-TAYaAGhh-9xNG-9rMNEZHQRElvdDletx0&lib=MlJcTt87ug5f_XmzO-tnIbN3yFe7Nfhi6')
#     Choice =  (r.json()) 
#     course = Choice[0]['course_name']
#     print(course)
#     x = len(Choice[0]['slots'])
#     for i in range(x):
#         your_dt = datetime.datetime.fromtimestamp(int(Choice[0]['slots'][i]['slot'])/1000)
#         slot = (your_dt.strftime("%Y-%m-%d"))
#         slot_save = Slots.objects.create(course=course,slot=slot)
#         slot_save.save()


    