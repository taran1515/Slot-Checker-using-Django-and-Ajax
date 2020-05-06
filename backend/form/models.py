from datetime import datetime,timedelta 
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Slots(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slot_date = models.DateField(default=datetime.now().date)

    def __str__(self):
        return str(self.slot_date)

class TrialClass(models.Model):

    parents_name = models.CharField(max_length=50)
    parents_contact_no = models.CharField(max_length=10)
    parents_email_id = models.EmailField()
    child_name = models.CharField(max_length=50)
    child_age = models.IntegerField()
    course = models.ForeignKey(Course,on_delete=models.SET_NULL, null=True)
    slot = models.ForeignKey(Slots,on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.child_name