from django.contrib import admin
from .models import Slots,Course, TrialClass, TimeSlots

admin.site.register(Course)
admin.site.register(Slots)
admin.site.register(TimeSlots)
admin.site.register(TrialClass)