from datetime import datetime,timedelta 
from django.db import models
import requests



class Course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Slots(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slot_date = models.DateField(default=datetime.now().date)

    def __str__(self):
        return str(self.slot_date)

class TimeSlots(models.Model):
    slot = models.ForeignKey(Slots, on_delete=models.CASCADE)
    time_slot = models.TimeField(default=datetime.now().time)

    def __str__(self):
        return str(self.slot)+'-'+str(self.time_slot)

class TrialClass(models.Model):

    parents_name = models.CharField(max_length=50,null=False)
    parents_contact_no = models.CharField(max_length=10,null=False)
    parents_email_id = models.EmailField(null=False)
    child_name = models.CharField(max_length=50,null=False)
    child_age = models.IntegerField(null=False)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL, null=True)
    slot = models.ForeignKey(Slots,on_delete=models.SET_NULL, null=True)
    time_slot = models.ForeignKey(TimeSlots,on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.child_name

